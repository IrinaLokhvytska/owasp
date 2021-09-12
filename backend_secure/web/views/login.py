from flask.views import MethodView
from flask import render_template

class LoginAPI(MethodView):
    """ View for the /login endpoint """
    def get(self):
        """ Get login page """
        return render_template('home.html')

    # def post(self):
    #     user = User.from_form_data(request.form)
