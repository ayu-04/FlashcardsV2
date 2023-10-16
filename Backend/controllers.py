from re import U
from flask import  jsonify, request
from flask_cors import CORS
import pyexcel as pe
from flask import make_response
from flask import current_app as app
from flask_login import login_user, login_required, logout_user
from models import user,decks,cards,db
from data import Cards
from datetime import datetime
from main import cache
import io 
import redis

#---------------App-------------------

#enable cors
CORS(app, resources={r'/*': {'origins': '*'}})

#--------------------USER API-------------------------

#login
@app.route('/',methods=['GET','POST'])
def login():
	if request.method=='GET':
		return '',200
	response_obj={'u_name':None}
	if request.method=='POST':
		#get post data
		post_data = request.get_json()
		u_name=post_data.get('username')
		p_word=post_data.get('password')
		#query user
		u=user.query.filter_by(username=u_name).first()
		#if user doesn't exist
		if u==None:
			return '',404
		#if correct password
		elif u.password==p_word:
			response_obj['u_name']=u_name
			login_user(u,remember=True)
			return jsonify(response_obj),200
		#if incorrect password
		else:
			return '',404

#signup
@app.route('/create_account',methods=['GET','POST'])
def create_acc():
	if request.method=='GET':
		return '',200
	response_obj={'u_name':None}

	if request.method=='POST':
		#get post data
		post_data = request.get_json()
		u_name=post_data.get('username')
		p_word=post_data.get('password')
		e_mail=post_data.get('email')
		#query user
		u=user.query.filter_by(username=u_name).first()
		#if user exists
		if u!=None:
			return '',404
		#if user doesn't exist
		else:
			#add user
			u=user(username=u_name,password=p_word,email=e_mail)
			db.session.add(u)
			db.session.commit()

			for c in Cards:
				#add default decks
				d=decks(username=u_name,title=c,rec_score=None,date_time=None)
				db.session.add(d)
				db.session.commit()
				#add cards
				for j in range(len(Cards[c])):
					x=cards(username=u_name,title=c,card_no=j,question=Cards[c][j][0],answer=Cards[c][j][1],score=None)
					db.session.add(x)
					db.session.commit()

			login_user(u,remember=True)
			
			response_obj['u_name']=u_name
	return jsonify(response_obj),200

#dashboard
@app.route('/dashboard/<u_name>',methods=['GET'])
def dashboard(u_name):
	if request.method=='GET':
		u_name=str(u_name)
		#query user
		u=user.query.filter_by(username=u_name).first()
		#fetch cached decks
		user_cards=decks_cached(u.username)
		do_it_again=[]
		try_smtg_new=[]
		for i in user_cards:
			if i.date_time!=None:
				d=i.__dict__
				del d['_sa_instance_state']
				do_it_again.append(d)
			else:
				d=i.__dict__
				del d['_sa_instance_state']
				try_smtg_new.append(d)
		do_it_again.sort(reverse=True,key=lambda x:x['date_time'])
		
		return jsonify({'do_it_again':do_it_again,'try_smtg_new':try_smtg_new,'username':u.username}),200

#logout
@app.route('/logout',methods=['POST'])
def logout():
	logout_user()
	return '',200

#--------------------flashcard------------------------

@app.route('/<string:u_name>/flashcard/<string:t>/0',methods=['GET','POST'])
def flashcard(u_name,t):
	#delete cached decks
	cache.delete_memoized(decks_cached,u_name)
	#format datetime
	d_t=datetime.now().strftime('%Y-%m-%d %H:%M')
	d_t=datetime.strptime(d_t,'%Y-%m-%d %H:%M')
	#update deck
	d=decks.query.filter_by(username=u_name,title=t).first()
	d.rec_score=0
	db.session.commit()
	d.date_time=d_t
	db.session.commit()
	#fetch cached cards
	c=cards_cached(u_name,t)
	for i in c:
		i.score=0
		db.session.commit()
	
	if len(c)>0:
		return card(u_name,t,0)
	else:
		return '',404

@app.route('/<string:u_name>/flashcard/<string:t>/<int:i>',methods=['GET','POST'])
def card(u_name,t,i):
	#fetch cached cards
	c=cards_cached(u_name,t)
	tot_cards=len(c)
	#query deck
	d=decks.query.filter_by(username=u_name,title=t).first()
	if len(c)>i:
		if request.method=='GET':
			card=c[i].__dict__
			del card['_sa_instance_state']
			return jsonify({'username':d.username,'c_no':i,'c':card,'score':d.rec_score, 'tot_cards': tot_cards}),200
		
		if request.method=='POST':
			#get post data
			post_data = request.get_json()
			u_name=post_data.get('username')
			t=post_data.get('title')
			c_no=post_data.get('card_no')
			sc=post_data.get('score')
			rec_sc=post_data.get('rec_score')
			#update card
			c=cards.query.filter_by(username=u_name,title=t,card_no=c_no).first()
			c.score=sc
			db.session.commit()
			d.rec_score=rec_sc
			db.session.commit()
			
			return jsonify({'rec_score':d.rec_score}),200
	else:
		return '',404

#------------------------DECKS API--------------------

#get decks & post decks
@app.route('/<string:u_name>/decks',methods=['GET','POST'])
def decks_api(u_name):
	if request.method=='GET':
		#fetch cached decks
		user_cards=decks_cached(u_name)
		dict=[]
		for i in user_cards:
			d=i.__dict__
			del d['_sa_instance_state']
			dict.append(d)
		return jsonify({'decks':dict}),200
	if request.method=='POST':
		#get post data
		post_data = request.get_json()
		t=post_data.get('title')
		no_of_cards=int(post_data.get('no_of_cards'))
		#query deck
		d=decks.query.filter_by(username=u_name,title=t).first()
		#if deck exists
		if d!=None:
			return '',404
		#if deck doesn't exist
		else:
			#add deck
			d=decks(username=u_name,title=t,rec_score=None,date_time=None)
			db.session.add(d)
			db.session.commit()
			#delete cached decks
			cache.delete_memoized(decks_cached,u_name)
			return '',200

#delete deck
@app.route('/<string:u_name>/decks/<string:t>',methods=['DELETE'])
def delete_deck(u_name,t):
	#fetch cached decks
	d=decks_cached(u_name)
	
	if request.method=='DELETE':
		#fetch cached cards
		c=cards_cached(u_name,t)
		#delete cards
		for j in c:
			db.session.delete(j)
			db.session.commit()
		#delete cached cards
		cache.delete_memoized(cards_cached,u_name,t)

		#delete deck
		d=decks.query.filter_by(username=u_name,title=t).first()
		db.session.delete(d)
		db.session.commit()
		#delete cached decks
		cache.delete_memoized(decks_cached,u_name)
		return '',200

#export decks
@app.route('/<string:u_name>/export',methods=['POST'])
def export_decks(u_name):
	if request.method=='POST':
		#get post data
		post_data = request.get_json()
		t=post_data.get('title')
		#fetch cached cards
		c=cards_cached(u_name,t)
		x=[]
		for i in c:
			x.append([i.question,i.answer])
		#convert into csv file
		t_file=t+'.csv'
		sheet = pe.Sheet(x)
		Io = io.StringIO()
		sheet.save_to_memory("csv", Io)
		output = make_response(Io.getvalue())
		output.headers["Content-Disposition"] = "attachment; filename="+t_file
		output.headers["Content-type"] = "text/csv"
		return output, 200

#----------------------CARDS API--------------------------	

#get cards & post cards
@app.route('/<string:u_name>/cards/<string:t>',methods=['GET','POST'])
def cards_get_post(u_name,t):
	#fetch cached cards
	c=cards_cached(u_name,t)
	
	if request.method=='GET':
		dict=[]
		for i in c:
			d=i.__dict__
			del d['_sa_instance_state']
			dict.append(d)
		return jsonify({'c':dict}),200
	
	if request.method=='POST':
		#get post data
		post_data = request.get_json()
		ques=post_data.get('question')
		ans=post_data.get('answer')
		
		last=c[-1].card_no
		#add card
		d=decks.query.filterby(username=u_name, title=t)
		d.total_cards=len(c)+1
		x=cards(username=u_name,title=t,card_no=last+1,question=ques,answer=ans)
		db.session.add(x)
		db.session.commit()
		#delete cached cards
		cache.delete_memoized(cards_cached,u_name,t)
		return '',200

#-------------------CARD API------------------------

#get card & post card & put card & delete card
@app.route('/<string:u_name>/card/<string:t>/<int:c_no>',methods=['GET','POST','PUT','DELETE'])
def card_api(u_name,t,c_no):
	if request.method=='GET':
		c=cards.query.filter_by(username=u_name,title=t,card_no=c_no).first()
		return jsonify({'question':c.question,'answer':c.answer}),200
	if request.method=='POST':
		#delete cached cards
		cache.delete_memoized(cards_cached,u_name,t)
		#get post data
		post_data = request.get_json()
		ques=post_data.get('question')
		ans=post_data.get('answer')
		#add card
		c=cards(username=u_name,title=t,card_no=c_no,question=ques,answer=ans,score=0)
		db.session.add(c)
		db.session.commit()
		return '',200
	if request.method=='PUT':
		#delete cached cards
		cache.delete_memoized(cards_cached,u_name,t)
		#query cards
		c=cards.query.filter_by(username=u_name,title=t,card_no=c_no).first()
		#get post data
		post_data = request.get_json()
		ques=post_data.get('question')
		ans=post_data.get('answer')
		#update card
		c.question=ques
		db.session.commit()
		c.answer=ans
		db.session.commit()
		return '',200
	if request.method=='DELETE':
		#delete cached cards
		cache.delete_memoized(cards_cached,u_name,t)
		#delete card
		c=cards.query.filter_by(username=u_name,title=t,card_no=c_no).first()
		db.session.delete(c)
		db.session.commit()
		return '',200 

#-------------------Caching----------------------------

@cache.memoize(50)
def decks_cached(u_name):
	d=decks.query.filter_by(username=u_name).all()
	return d

@cache.memoize(50)
def cards_cached(u_name,t):
	c=cards.query.filter_by(username=u_name,title=t).all()
	return c
	