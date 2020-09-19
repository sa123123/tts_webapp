from flaskweb import db


class User(db.Model):
    firstname= db.Column(db.String(1000),nullable=False)
    lastname=db.Column(db.String(1000))
    email =db.Column(db.String(100), unique=True,nullable=False)
    password =db.Column(db.String(100),nullable=False)
    number=db.Column(db.Integer,primary_key=True,nullable=False)

    def __repr__(self):
        return f"User('{self.firstname}','{self.lastname}','{self.email}','{self.password}','{self.number}')"
