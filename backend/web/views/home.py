"""Views for the / endpoint"""
from collections import defaultdict

from flask.views import MethodView
from flask import render_template, session

from web.helpers import check_login
from web.models.todo import ToDo


class HomeAPI(MethodView):
    """Views for the / endpoint"""

    @check_login
    def get(self):
        """Get home page"""
        user_id = session.get("user_id")
        todo_status = [
            {"id": "todo", "name": "To Do"},
            {"id": "in_progress", "name": "In Progress"},
            {"id": "done", "name": "Done"},
        ]
        todos = (
            ToDo.query.filter_by(user_id=user_id).order_by(ToDo.priority.desc()).all()
        )
        todo_list = defaultdict(list)
        for todo in todos:
            todo_dict = todo.get_todo_dict()
            todo_list[todo_dict["status"]].append(todo_dict)
        return render_template(
            "home.html", user_id=user_id, todo_status=todo_status, todo_list=todo_list
        )
