from flask import Blueprint, flash, request, redirect, render_template, url_for
from ..services.auth_service import AuthService
from flask_mail import Message # type: ignore
from ..extentions import mail

auth_bp = Blueprint('users', __name__, url_prefix="/api/v1/auth")

@auth_bp.route('/register/', methods=('GET', 'POST'))
def register():
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
            print(user)
            return render_template('register.html', message = "User with same email already exists"), 400
        
        user = user['user']
        msg = Message(
            subject="Registration Mail",
            sender="patelhet2652004@gmail.com.com",
            recipients=[f"{ user['email'] }"]
        )
        
        msg.body = "Hello, Registration Completed"
        mail.send(msg)
        
        return redirect(url_for('users.login')), 200
        
    return render_template('register.html', message = None), 200

@auth_bp.route('/login/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        data = AuthService.validate_user_password(email = email, password = password)
        if 'error' in data:
            return render_template('login.html', message = "Wrong credentials, User with this email and password not found"), 404
        
        return render_template('dashboard.html', user = data['user'])
    
    return render_template('login.html', message = None), 200