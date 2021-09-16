""" Endpoints for the todo API """
from flask.views import MethodView
from flask import (
    render_template, session
)
from sqlalchemy.exc import IntegrityError

from web.models import db
from web.helpers import check_login


class ToDoAPI(MethodView):
    """ Endpoints for the todo API """
    @check_login
    def get(self, todo_id):
        """ Get todo item info """
        with db.engine.connect() as connection:
            todo_item = connection.execute(f"SELECT * FROM todo_list WHERE id={todo_id}").first()
        return render_template(
            'todo.html',
            user_id=session.get("user_id"),
            todo_item=todo_item
        )

    def delete(self, todo_id):
        """ Get todo item info """
        try:
            with db.engine.connect() as connection:
                todo_item = connection.execute(f"DELETE * FROM todo_list WHERE id={todo_id}")
                db.session.flush()
                db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return "The todo was deleted"
