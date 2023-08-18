class Post:

    def __init__(self, text: str, author: User, day: date):
        self.text = text
        self.author = author
        self.day = day