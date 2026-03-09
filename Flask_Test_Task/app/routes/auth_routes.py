from flask import Blueprint, flash, request, redirect, render_template, url_for, session
from ..services.auth_service import AuthService
from flask_mail import Message # type: ignore
from ..extentions import mail

auth_bp = Blueprint('users', __name__, url_prefix="/api/v1/auth")
user = None

@auth_bp.route('/register/', methods=('GET', 'POST'))
def register():
    """
    Responds to get and post request on rout /api/v1/auth/register
    creates new user on post request and renders registration form on get request
    """
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        hobbies = request.form.getlist('option')
        gender = True if request.form['gender'] == 'male' else False
        
        user = AuthService.create_user(first_name = first_name, last_name = last_name,
                                       email= email, password = password, address = address,
                                       hobbies = hobbies, gender = gender)
        if 'error' in user:
            return render_template('register.html', message = user['error']), 400
        
        user = user['user']
        msg = Message(
            subject="Registration Mail",
            sender="patelhet2652004@gmail.com.com",
            recipients=[f"{ user['email'] }"]
        )
        
        msg.body = "Hello, Registration Completed"
        mail.send(msg)
        
        return redirect( url_for('users.login') )
        
    return render_template('register.html', message = None), 200

@auth_bp.route('/login/', methods=('GET', 'POST'))
def login():
    """
    Responds to get and post request on rout /api/v1/auth/login
    login user on post request and renders login form on get request
    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        data = AuthService.validate_user_password(email = email, password = password)
        if 'error' in data:
            msg = data['error']
            return render_template('login.html', message = msg), 404
        
        session['user'] = data['user']
        print(data['user']['hobbies'])
        return redirect( url_for('users.dashboard') )
    
    return render_template('login.html', message = None), 200

@auth_bp.route('/dashboard/', methods = ('GET', 'POST'))
def dashboard():
    """
    Responds to get and post request on rout /api/v1/auth/dashboard
    edit user details on post request and renders user details card on get request
    """
    
    if request.method == 'POST':
        f_name = request.form.get('e_first_name')
        l_name = request.form.get('e_last_name')
        address = request.form.get('e_address')
        hobbies = request.form.getlist('e_option')
        gender = True if request.form.get('e_gender') == 'male' else False
        password = request.form.get('password')
        
        user = AuthService.updateUser(email = session['user']['email'],first_name = f_name, last_name = l_name, address = address, hobbies = hobbies, gender = gender, password = password)
        session['user'] = user
        
        if 'error' in user:
            msg = user['error']
            return render_template('dashboard.html', user = session['user'],message = msg), 404
        
        return render_template('dashboard.html', user = session['user']), 200
    
    return render_template('dashboard.html', user = session['user']), 200


