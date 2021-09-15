from flask.views import MethodView
from flask import render_template, session

from web.helpers import check_login
from web.models.user import User


class AdminAPI(MethodView):
    """ Views for the /admin endpoint """
    @check_login
    def get(self):
        """ Get admin page """
        users = []
        db_users = User.query.filter_by().all()
        for user in db_users:
            users.append({
                "id": user.id,
                "email": user.email,
                "password": user.password,
                "registered_on": user.registered_on,
                "role": "admin" if user.admin else "regular user"
            })
        return render_template(
            'admin.html',
            user_id=session.get("user_id"),
            users=users,
        )
