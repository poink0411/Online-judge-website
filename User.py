from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, email, name, password):
        self.id=id
        self.email=email
        self.name=name
        self.password=password
    def get_id(self):
        return self.id
    def __repr__(self):
        return f"USER: {self.id} = {self.name}"