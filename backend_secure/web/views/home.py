""" Render home page """
from collections import defaultdict

from flask.views import MethodView
from flask import render_template, session, request, jsonify, redirect, url_for

from web.helpers import check_user_token, check_user_token
from web.models.todo import ToDo


class HomeAPI(MethodView):
    """ Views for the / endpoint """
    def get(self):
        """ Get home page """
        jwt_payload = check_user_token()
        if "answer" in jwt_payload:
            return redirect(url_for("login"))
        print(jwt_payload)
        user_id = jwt_payload.get("user_id")
        todo_status = [
            {"id": "todo", "name": "To Do"},
            {"id": "in_progress", "name": "In Progress"},
            {"id": "done", "name": "Done"},
        ]
        todos = ToDo.query.filter_by(
            user_id=user_id
        ).order_by(ToDo.priority.desc()).all()
        todo_list = defaultdict(list)
        for todo in todos:
            todo_dict = todo.get_todo_dict()
            todo_list[todo_dict["status"]].append(todo_dict)
        return render_template(
            'home.html',
            user_id=user_id,
            todo_status=todo_status,
            todo_list=todo_list
        )
