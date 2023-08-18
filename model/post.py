from datetime import date
from model.user import User
class Text:

    def __init__(self, text: str, author: User):
        self.text = text
        self.author = author
        self.day = date.today()