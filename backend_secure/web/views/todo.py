"""Endpoints for the todo API"""
from flask.views import MethodView
from flask import render_template, session, jsonify, request
from flask import current_app as app
from sqlalchemy.exc import IntegrityError

from web.models import db
from web.models.todo import ToDo
from web.helpers import check_login


PRIORITY_TO_INT = {"low": 0, "medium": 1, "high": 2}
STATUS_TO_INT = {"todo": 0, "in_progress": 1, "done": 2}


class AddToDoAPI(MethodView):
    """Endpoints for the add todo API"""

    @check_login
    def post(self):
        """Add todo item info"""
        data = request.json
        try:
            todo_item = ToDo(
                title=data.get("title"),
                description=data.get("description"),
                image=data.get("image"),
                user_id=session.get("user_id"),
                status=STATUS_TO_INT[data.get("status")] if data.get("status") else 0,
                priority=PRIORITY_TO_INT[data.get("priority")]
                if data.get("priority")
                else 0,
            )
            db.session.add(todo_item)
            db.session.flush()
            db.session.commit()
        except IntegrityError as exc:
            app.logger.error(str(exc))
            db.session.rollback()
            return jsonify({"answer": "error", "msg": str(exc)}), 500
        return jsonify({"answer": "success"}), 200


class ToDoAPI(MethodView):
    """Endpoints for the todo API"""

    @check_login
    def get(self, todo_id):
        """Get todo item info"""
        todo_item = ToDo.query.filter_by(
            id=todo_id, user_id=session.get("user_id")
        ).first()
        if not todo_item:
            return (
                jsonify({"answer": "error", "msg": "You do not have permission"}),
                500,
            )
        return render_template(
            "todo.html",
            user_id=session.get("user_id"),
            todo_item=todo_item.get_todo_dict(),
        )

    @check_login
    def delete(self, todo_id):
        """Delete todo item info"""
        try:
            ToDo.query.filter_by(id=todo_id, user_id=session.get("user_id")).delete()
            db.session.flush()
            db.session.commit()
        except IntegrityError as exc:
            app.logger.error(str(exc))
            db.session.rollback()
            return jsonify({"answer": "error", "msg": str(exc)}), 500
        return jsonify({"answer": "success"}), 200

    @check_login
    def put(self, todo_id):
        """Update todo item info"""
        data = request.json
        try:
            ToDo.query.filter_by(id=todo_id, user_id=session.get("user_id")).update(
                dict(
                    title=data.get("title"),
                    description=data.get("description"),
                    image=data.get("image"),
                    status=STATUS_TO_INT[data.get("status")]
                    if data.get("status")
                    else 0,
                    priority=PRIORITY_TO_INT[data.get("priority")]
                    if data.get("priority")
                    else 0,
                )
            )
            db.session.flush()
            db.session.commit()
        except IntegrityError as exc:
            app.logger.error(str(exc))
            db.session.rollback()
            return jsonify({"answer": "error", "msg": str(exc)}), 500
        return jsonify({"answer": "success"}), 200
