"""Add endpoints to the app"""
from web.views import login, home, user, admin, todo


def add_endpoints_to_app(app):
    """Add endpoints to the app"""
    app.add_url_rule('/', view_func=home.HomeAPI.as_view('home'))
    app.add_url_rule('/login', view_func=login.LoginAPI.as_view('login'))
    app.add_url_rule('/logout', view_func=login.LogoutAPI.as_view('logout'))
    app.add_url_rule('/user', view_func=user.RegistrationAPI.as_view('register'))
    app.add_url_rule('/admin', view_func=admin.AdminAPI.as_view('admin'))
    app.add_url_rule('/user/<int:user_id>', view_func=user.UserAPI.as_view('user'))
    app.add_url_rule('/todo', view_func=todo.AddToDoAPI.as_view('todo'))
    app.add_url_rule('/todo/<int:todo_id>', view_func=todo.ToDoAPI.as_view('todo_info'))
