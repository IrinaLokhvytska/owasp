""" Add endpoints to the app """
from web.views import login, home

def add_endpoints_to_app(app):
    """ Add endpoints to the app """
    app.add_url_rule('/', view_func=home.HomeAPI.as_view('home'))
    app.add_url_rule('/login', view_func=login.LoginAPI.as_view('login'))
    app.add_url_rule('/logout', view_func=login.LogoutAPI.as_view('logout'))
