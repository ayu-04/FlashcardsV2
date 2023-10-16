from flask import Flask
from models import db,user,cards,decks,login
from flask_caching import Cache
from workers import make_celery

app=Flask(__name__)  

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashcards.sqlite3'
app.config['SECRET_KEY'] = 'secretkey'
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
app.config['CACHE_TYPE']='RedisCache'
app.config['CACHE_REDIS_HOST']='localhost'
app.config['CACHE_REDIS_PORT']='6379'

db.init_app(app)
app.app_context().push()
login.init_app(app)
app.app_context().push()
cache=Cache(app)
app.app_context().push()
celery = make_celery(app)
app.app_context().push()

from controllers import *

app.run(host='0.0.0.0',port='5000')