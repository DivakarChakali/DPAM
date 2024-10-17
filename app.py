from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
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
  response = app.make_response(render_template('home.html'))
  response.headers['Cache-Control'] = 'max-age=180'
  return response

@app.route('/services')
def services():
  response = app.make_response(render_template('services.html'))
  response.headers[
      'Cache-Control'] = 'max-age=180'  # Example: Cache for 1 hour
  return response

@app.route('/services/office-shifting')
def office_relocation():
  response = app.make_response(render_template('services/office-relocation.html'))
  response.headers[
      'Cache-Control'] = 'public, max-age=3600'  # Example: Cache for 1 hour
  return response

@app.route('/services/domestic-shifting')
def household_shifting():
  response = app.make_response(
      render_template('services/domestic-shifting.html'))
  response.headers[
      'Cache-Control'] = 'public, max-age=180'  # Example: Cache for 1 hour
  return response


@app.route('/services/loading-and-unloading')
def loading_unloading():
  response = app.make_response(
      render_template('services/loading-unloading.html'))
  response.headers[
      'Cache-Control'] = 'public, max-age=3600'  # Example: Cache for 1 hour
  return response


@app.route('/services/packing-and-moving')
def packing_moving():
  response = app.make_response(
      render_template('services/packing-moving.html'))
  response.headers[
      'Cache-Control'] = 'public, max-age=3600'  # Example: Cache for 1 hour
  return response


@app.route('/services/pre-moving-survey')
def pre_moving_survey():
  response = app.make_response(
      render_template('services/pre-moving-survey.html'))
  response.headers[
      'Cache-Control'] = 'public, max-age=3600'  # Example: Cache for 1 hour
  return response


@app.route('/services/transportation')
def transportation():
  response = app.make_response(render_template('services/transportation.html'))
  response.headers[
      'Cache-Control'] = 'public, max-age=3600'  # Example: Cache for 1 hour
  return response

@app.route('/about')
def about():
  response = app.make_response(render_template('about.html'))
  response.headers[
      'Cache-Control'] = 'public, max-age=180'  # Example: Cache for 1 hour
  return response


@app.route('/contact-us')
def contact_us():
  response = app.make_response(render_template('contact-us.html'))
  response.headers[
      'Cache-Control'] = 'public, max-age=180'  # Example: Cache for 1 hour
  return response


@app.route('/faq')
def faq():
  response = app.make_response(render_template('faq.html'))
  response.headers[
      'Cache-Control'] = 'public, max-age=180'  # Example: Cache for 1 hour
  return response

@app.route('/submitrform', methods=['POST'])
def submitrform():
  # Get form data
  name = request.form['name']
  email = request.form['email']
  phone = request.form['phone']
  moving_date = request.form['moving_date']
  origin = request.form['origin']
  destination = request.form['destination']
  special_requests = request.form['special_requests']

  # Server-side validation
  email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
  phone_pattern = r'^\d{10}$'
  errors = []

  if not name:
    errors.append('Name is required')
  if not re.match(email_pattern, email):
    errors.append('Invalid email format')
  if not re.match(phone_pattern, phone):
    errors.append('Invalid phone number format')
  if not moving_date:
    errors.append('Moving date is required')

  if errors:
    return render_template('home.html', errors=errors)
  else:
    try:
      request_notification(name, email, phone, moving_date, origin, destination,
                         special_requests)
      # Flash a success message
      flash("Your quotation request has been submitted successfully!",
            "success")
      return redirect(url_for('home'))
    except Exception as e:
      return f'Error: {str(e)}'


@app.route('/submitcform', methods=['POST'])
def submitcform():
  name = request.form['cname']
  email = request.form['cemail']
  message = request.form['cmessage']
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
      contact_notification(name, email, message)
      # Flash a success message
      flash("Your contact request has been submitted successfully!", "success")
      return redirect(url_for('home'))
    except Exception as e:
      return f'Error: {str(e)}'


def contact_notification(cname, cemail, cmessage):
  msg = Message(subject='contact request conformation', recipients=[cemail])
  msg.html = render_template('email-templates/cmail.html',
                             name=cname,
                             email=cemail,
                             message=cmessage)
  mail.send(msg)
  adminNC(cname, cemail, cmessage,admail)


def request_notification(name, email, phone, moving_date, origin, destination,
                       special_requests):
  msg = Message(subject='Acknowledgement from Divakarpackersandmover.com',
                recipients=[email])
  msg.html = render_template('email-templates/rmail.html',
                             name=name,
                             email=email,
                             phone=phone,
                             moving_date=moving_date,
                             origin=origin,
                             destination=destination,
                             special_requests=special_requests)
  mail.send(msg)
  adminNR(name, email, phone, moving_date, origin, destination,admail)


def adminNC(cname, cemail, cmessage,admail):
  msg = Message(subject='New contact request received', recipients=[admail])
  msg.html = render_template('email-templates/amc.html',
                             name=cname,
                             email=cemail,
                             message=cmessage)
  mail.send(msg)


def adminNR(name, email, phone, moving_date, origin, destination,admail):
  msg = Message(subject='New quotation request received', recipients=[admail])
  msg.html = render_template('email-templates/amr.html',
                             name=name,
                             email=email,
                             phone=phone,
                             moving_date=moving_date,
                             origin=origin,
                             destination=destination)
  mail.send(msg)

def add_x_content_type_options(response):
  response.headers['X-Content-Type-Options'] = 'nosniff'
  return response


# Register the function as an 'after_request' handler
app.after_request(add_x_content_type_options)


def set_x_content_type_options_header(response):
  response.headers['X-Content-Type-Options'] = 'nosniff'
  return response


# Register the function as an 'after_request' handler
app.after_request(set_x_content_type_options_header)


def modify_server_header(response):
  response.headers['Server'] = 'MyServer'
  return response


# Register the function as an 'after_request' handler
app.after_request(modify_server_header)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
