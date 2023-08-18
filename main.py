from flask import Flask, jsonify, request
import json
from model.post import Text
from model.comment import Comment


app = Flask(__name__)
dict_posts = {}


class MyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Text):
            return {"text": obj.text, "author": obj.author, "day": obj.day.isoformat()}
        elif isinstance(obj, Comment):
            return {"author": obj.author, "comment": obj.comment_body, "day": obj.day.isoformat()}
        else:
            return super().default(obj)

app.json_encoder = MyJSONEncoder
@app.route('/ping')
def ping():
    return jsonify({'response': 'pong'})


@app.route('/post', methods=['POST'])
def create_post():
    post_json = request.get_json()
    post = Text(post_json['text'], post_json['author'])
    dict_posts[post.text] = {'author': post.author, 'day': post.day.isoformat(), 'comments': []}
    return jsonify({'status': 'success'})


@app.route('/post/comment', methods=['POST']) ####НЕ ДОДЕЛАЛА
def create_comment():
    comment_json = request.get_json()
    comment = Comment(comment_json['author'], comment_json['comment_body'])
    dict_posts[comment_json['text']]['comments'].append(comment)
    return jsonify({'status': 'success'})


@app.route('/post', methods=['DELETE'])
def delete_posts():
    to_del_json = request.get_json()
    key_to_del = to_del_json['text']
    del dict_posts[key_to_del]
    return jsonify({'status': 'success'})


@app.route('/post', methods=['GET'])
def read_posts():
    return jsonify({'posts': dict_posts})


@app.route('/post/comment', methods=['GET'])
def read_comments():
    return jsonify({'all_data': dict_posts})

if __name__ == '__main__':
    app.run(debug=True)