"""To Do List db model"""
import datetime

from web.models import db


PRIORITY = {0: "low", 1: "medium", 2: "high"}
STATUS = {0: "todo", 1: "in_progress", 2: "done"}


class ToDo(db.Model):
    """ToDo Model for storing todo list related details"""
    __tablename__ = "todo_list"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_on = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    priority = db.Column(db.Integer, nullable=False, default=0)
    image = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, title, description, image, user_id, status=0, priority=0):
        """Init ToDo db model"""
        self.title = title
        self.description = description
        self.created_on = datetime.datetime.now()
        self.status = status
        self.priority = priority
        self.image = image
        self.user_id = user_id

    def get_todo_dict(self):
        """Convert priority and status, return dict"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_on": self.created_on.strftime("%m/%d/%Y"),
            "status": STATUS[self.status],
            "priority": PRIORITY[self.priority],
            "image": self.image if self.image else "images/default_todo_image.jpeg"
        }
