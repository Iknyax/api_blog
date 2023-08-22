from datetime import date
from model.user import User

class Comment:
    def __init__(self, comment_body: str, author: User):
        self.comment_body = comment_body
        self.author = author
        self.day = date.today()

