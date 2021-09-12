from flask.views import MethodView
from flask import render_template

from web.helpers import check_login


class HomeAPI(MethodView):
    """ Views for the / endpoint """
    @check_login
    def get(self):
        """ Get home page """
        return render_template('layout.html')
