from OrganizeMe import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=True)
    groups = db.relationship('Group', backref='user', lazy=True)

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(20), nullable=True)
    todos = db.relationship('Todo', backref='group',  lazy=True)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.Integer, nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)

