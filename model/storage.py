from model.post import Post


class StorageException(Exception):
    pass

class Storage:
    def __init__(self):
        self.dict = {}
        self.id_counter = 0



    def create_post(self, post: Post):    #записали пост в хранилище
        self.id_counter += 1
        self.dict[str(self.id_counter)] = post
        return str(self.id_counter)



    def read_post(self, post_id: str):    #выдаем пост из хранилища
        try:
            return self.dict[post_id]
        except Exception:
            raise StorageException('no such post')


    def read_all_posts(self):
        return self.dict



    def delete_post(self, post_id: str):
        try:
            del self.dict[post_id]
        except Exception:
            raise StorageException('no such post')




#def create_comment():
#    comment_json = request.get_json()
 #   comment = Comment(comment_json['author'], comment_json['comment_body'])
  #  dict_posts[comment_json['text']]['comments'].append(comment)
   # return jsonify({'status': 'success'})





#def read_comments():
 #   return jsonify({'all_data': dict_posts})