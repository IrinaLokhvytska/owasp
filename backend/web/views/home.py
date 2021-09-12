from flask.views import MethodView
from flask import render_template


class HomeAPI(MethodView):
    """ Views for the / endpoint """
    def get(self):
        """ Get home page """
        return render_template('layout.html')
