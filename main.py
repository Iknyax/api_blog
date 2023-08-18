from flask import Flask, jsonify, request
import json
from model.post import Text


app = Flask(__name__)
dict_posts = []


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Text):
            return {"text": obj.text, "author": obj.author, "day": obj.day.isoformat()}
        else:
            return super().default(obj)

app.json_encoder = CustomJSONEncoder
@app.route('/ping')
def ping():
    return jsonify({'response': 'pong'})


@app.route('/post', methods=['POST'])
def create_post():
    post_json = request.get_json()
    post = Text(post_json['text'], post_json['author'])
    dict_posts.append(post)
    return jsonify({'status': 'success'})



@app.route('/post', methods=['GET'])
def read_posts():
    return jsonify({'posts': dict_posts})



if __name__ == '__main__':
    app.run(debug=True)