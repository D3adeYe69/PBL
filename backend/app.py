from flask import Flask, jsonify, url_for, render_template,request
from project import create_app,db

app = create_app()




@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created!'}), 201



if __name__ == '__main__':
    app.run(debug=True)