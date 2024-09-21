from flask import Flask, jsonify, url_for, render_template,request
from project import create_app,db

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





if __name__ == '__main__':
    app.run(debug=True)