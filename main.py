from flask import Flask, jsonify
from datetime import date

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({'response': 'pong'})


if __name__ == '__main__':
    app.run(debug=True)