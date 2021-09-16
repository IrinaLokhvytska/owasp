from flask.views import MethodView
from flask import render_template, session, jsonify

from web.helpers import check_user_role, check_user_token
from web.models.user import User


class AdminAPI(MethodView):
    """ Views for the /admin endpoint """
    def get(self):
        """ Get admin page """
        jwt_payload = check_user_token()
        if "answer" in jwt_payload:
            return redirect(url_for("login"))
        if not check_user_role(jwt_payload.get("user_id")):
            return jsonify({"answer": "error", "msg": "You do not have permission"}), 500
        users = []
        db_users = User.query.filter_by().all()
        for user in db_users:
            users.append(user.get_user_info())
        return render_template(
            'admin.html',
            user_id=jwt_payload.get("user_id"),
            users=users,
        )
