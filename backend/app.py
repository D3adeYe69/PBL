from flask import Flask, jsonify, url_for, render_template, request, redirect
from project import create_app, db
from project.models import users  # Make sure to import your User model
import hashlib

app = create_app()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET'])
def sign_up():
    return render_template('sign-up.html')

@app.route('/choose', methods=['GET'])
def log_in():
    return render_template('choose.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')

    # Validate the data (you can expand this as needed)
    if len(username) < 3:
        return jsonify({"error": "Username must be at least 3 characters long"}), 400
    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters long"}), 400
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email address"}), 400

    # Check if the email is already in use
    existing_user = users.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "This email is already in use."}), 400

    # Encrypt the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Add the new user to the database
    new_user = users(username=username, password=hashed_password, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": True}), 201


def is_valid_email(email):
    # Simple email validation (you can enhance this)
    return "@" in email and "." in email

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Find user by email
    user = users.query.filter_by(email=email).first()
    if user is None:
        return jsonify({"error": "Invalid email "}), 400
    
    # Hash the provided password and print it
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    print("Hashed password:", hashed_password)  # Temporary print for debugging

    if user.password != hashed_password:
        return jsonify({"error": "Invalid email or password"}), 400

    # Successful login logic here
    return jsonify({"success": True}), 200


if __name__ == '__main__':
    app.run(debug=True)
