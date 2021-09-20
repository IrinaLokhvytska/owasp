"""Run flask application"""
from web import app, db


def create_db_tables():
    """Create db tables"""
    if app.config['INIT_DB']:
        with app.app_context():
            db.create_all()
    return app


if __name__ == "__main__":
    app = create_db_tables()
    app.run(host='0.0.0.0', port=5003)
