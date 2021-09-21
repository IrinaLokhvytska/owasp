"""Endpoints for the todo API"""
from flask.views import MethodView
from flask import (
    render_template, session, jsonify, request
)
from flask import current_app as app
from sqlalchemy.exc import IntegrityError

from web.models import db
from web.models.todo import ToDo
from web.helpers import check_login


class AddToDoAPI(MethodView):
    """Endpoints for the add todo API"""
    @check_login
    def post(self):
        """Add todo item info"""
        data = request.json
        print(data)
        try:
            todo_item = ToDo(
                title=data.get("title"),
                description=data.get("description"),
                image=data.get("image"),
                user_id=session.get("user_id"),
                status=data.get("status"),
                priority=data.get("priority"),
            )
            db.session.add(todo_item)
            db.session.flush()
            db.session.commit()
        except IntegrityError as exc:
            app.logger.error(str(exc))
            db.session.rollback()
            return jsonify(
                {
                    "answer": "error",
                    "msg": str(exc)
                }), 500
        return jsonify({"answer": "success"}), 200


class ToDoAPI(MethodView):
    """Endpoints for the todo API"""
    @check_login
    def get(self, todo_id):
        """Get todo item info"""
        todo_item = ToDo.query.filter_by(id=todo_id).first()
        return render_template(
            'todo.html',
            user_id=session.get("user_id"),
            todo_item=todo_item.get_todo_dict()
        )

    @check_login
    def delete(self, todo_id):
        """Delete todo item info"""
        try:
            ToDo.query.filter_by(id=todo_id).delete()
            db.session.flush()
            db.session.commit()
        except IntegrityError as exc:
            app.logger.error(str(exc))
            db.session.rollback()
            return jsonify(
                {
                    "answer": "error",
                    "msg": str(exc)
                }), 500
        return jsonify({"answer": "success"}), 200
    
    @check_login
    def put(self, todo_id):
        """Update todo item info"""
        data = request.json
        try:
            ToDo.query.filter_by(id=todo_id).update(**data)
            db.session.flush()
            db.session.commit()
        except IntegrityError as exc:
            app.logger.error(str(exc))
            db.session.rollback()
            return jsonify(
                {
                    "answer": "error",
                    "msg": str(exc)
                }), 500
        return jsonify({"answer": "success"}), 200
