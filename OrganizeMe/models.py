from OrganizeMe import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=True)
    groups = db.relationship('Group', backref='user', lazy=True)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'groups': [group.id for group in self.groups]
        }

    def add_user(username, password, email):
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        return user

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(20), nullable=False)
    todos = db.relationship('Todo', backref='group',  lazy=True)

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'todos': [todo.id for todo in self.todos]
        }

    def add_group(user_id, name):
        group = Group(user_id=user_id, name=name)
        db.session.add(group)
        db.session.commit()
        return group

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    desc = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.Integer, nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)

    def to_json(self):
        return {
            'id': self.id,
            'group_id': self.group_id,
            'desc': self.desc,
            'priority': self.priority,
            'due_date': {
                'day': self.due_date.day,
                'month': self.due_date.month,
                'year': self.due_date.year
            }
        }

    def add_todo(desc, group_id, priority, due_date):
        todo = Todo(group_id=group_id, desc=desc, priority=priority, due_date=due_date)
        db.session.add(todo)
        db.session.commit()
        return todo