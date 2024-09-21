from flask import Flask, jsonify
from project import create_app
app = create_app()

@app.route('/', methods=['GET'])
def get_data():
    

    
    return jsonify({'message': 'hello website'})
if __name__ == '__main__':
    app.run(debug=True)