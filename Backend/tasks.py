from email.mime.base import MIMEBase
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from weasyprint import HTML
from jinja2 import Template
from email import encoders
from models import user,decks,cards,db
from datetime import datetime
from main import celery
from celery.schedules import crontab
from flask import current_app as app

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=16, minute=0), email_reminder_job.s(), name='Reminder')
    sender.add_periodic_task(crontab(hour=16, minute=0, day_of_month=13), email_report_job.s(), name='Report')

def send_mail(to, subject, message, file_attachment=None):
    msg=MIMEMultipart()
    msg['From']='ayu@ayu'
    msg['To']=to
    msg['Subject']=subject
    msg.attach(MIMEText(message, 'html'))
    if file_attachment:
        with open(file_attachment,'rb') as attachment:
            part=MIMEBase('application', 'octlet-stream')
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attactment; filename={file_attachment}')
        msg.attach(part)
    s=smtplib.SMTP(host='localhost', port='1025')
    s.login('ayu@ayu', 'ayu')
    s.send_message(msg)
    s.quit()
    return True
def format_message(template_file, u):
    f=open(template_file)
    template = Template(f.read())
    return template.render(u=u)

def send_reminder(u):
    message=format_message(r'C:\Users\shara\Desktop\Flashcards_v2\Backend\reminder.html', u)
    send_mail(u.email, subject='Reminder from Flashcards App', message=message)

@celery.task()
def email_reminder_job():
    with app.app_context():
        print('in job')
        for u in user.query.all():
            print(u.username)
            visited=False
            for d in decks.query.filter_by(username=u.username).all():
                if d.date_time:
                    diff=datetime.now()-d.date_time
                    duration_in_s = diff.total_seconds()
                    hours = divmod(duration_in_s, 3600)[0]
                    if hours<24:
                        visited=True
                        break
            if not visited:
            #celery tasks
                send_reminder(u)

def create_pdf_report(u,played,notplayed,tot):
    f=open(r'C:\Users\shara\Desktop\Flashcards_v2\Backend\Reportpdf.html')
    template = Template(f.read())
    report=template.render(u=u, played=played, notplayed=notplayed, tot=tot)
    html=HTML(string=report)
    file_name=u.username+'.pdf'
    html.write_pdf(target=file_name)
    return file_name

def send_report(u,played,notplayed,tot):
    message=format_message(r'C:\Users\shara\Desktop\Flashcards_v2\Backend\report.html', u)
    pdf=create_pdf_report(u,played,notplayed,tot)
    send_mail(u.email, subject='Report from Flashcards App', message=message, file_attachment=pdf)

@celery.task()
def email_report_job():
    with app.app_context():
        print('in job')
        for u in user.query.all():
            d=decks.query.filter_by(username=u.username).all()
            tot={}
            played=[]
            notplayed=[]
            for i in d:
                tot[i.title]=(len(cards.query.filter_by(username=u.username, title=i.title).all())*10)
                if i.date_time:
                    played.append(i)
                else:
                    notplayed.append(i)
            #celery tasks
            send_report(u,played,notplayed,tot)
