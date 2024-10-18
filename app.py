from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os, re, _json



app = Flask(__name__)

app.secret_key = os.environ.get('SECRETKEY')
admail = os.environ.get('amail')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('DEFAULT_SENDER')
app.config['MAIL_USERNAME'] = os.environ.get('username')
app.config['MAIL_PASSWORD'] = os.environ.get('Password')

mail = Mail(app)


@app.route('/')
def home():
  return render_template('index.html')

@app.route('/submitcform', methods=['POST'])
def submitcform():
  name = request.form['name']
  phone = request.form['phone']
  email = request.form['email']
  message = request.form['message']
  errors = []

  cemail_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

  if not name:
    errors.append('Name is required')
  if not re.match(cemail_pattern, email):
    errors.append('Invalid email format')

  if errors:
    return render_template('contactus.html', errors=errors)
  else:
    try:
      contact_notification(name, phone,email, message)
      # Flash a success message
      flash("Your contact request has been submitted successfully!", "success")
      return redirect(url_for('home'))
    except Exception as e:
      return f'Error: {str(e)}'


def contact_notification(cname, cphone,cemail, cmessage):
  msg = Message(subject='contact request conformation', recipients=[cemail])
  msg.html = render_template('email-templates/cmail.html',
                             name=cname,
                             phone=cphone,
                             email=cemail,
                             message=cmessage)
  mail.send(msg)
  adminNC(cname,cphone, cemail, cmessage,admail)


def adminNC(cname, cphone,cemail, cmessage,admail):
  msg = Message(subject='New contact request received', recipients=[admail])
  msg.html = render_template('email-templates/amc.html',
                             name=cname,
                             phone=cphone,
                             email=cemail,
                             message=cmessage)
  mail.send(msg)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
