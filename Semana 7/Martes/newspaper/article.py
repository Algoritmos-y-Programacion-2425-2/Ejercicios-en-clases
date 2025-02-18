class Article:
    def __init__(self, title, summary, body, creation_date, author):
        self.title = title
        self.summary = summary
        self.body = body
        self.images = []
        self.creation_date = creation_date
        self.approved_date = None
        self.author = author
        
    def show_article(self):
        return f"Title:\n{self.title}\nSummary:\n{self.summary}\nBody:\n{self.body}\nBy:{self.author}"