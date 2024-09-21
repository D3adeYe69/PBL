from flask import Flask, jsonify, url_for, render_template,request
from project import create_app,db

app = create_app()




@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)