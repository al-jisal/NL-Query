from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import openai


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initiates the database
    db.init_app(app)
    migrate.init_app(app, db)

    # creates the tables
    with app.app_context():
        from app.models import Student, Alum
        from app.data import students_data, alumni_data
        db.create_all()

        db.session.query(Student).delete()
        db.session.query(Alum).delete()

        # loads the data into the database
        db.session.bulk_insert_mappings(Student, students_data)
        db.session.bulk_insert_mappings(Alum, alumni_data)
        db.session.commit()

    # registers the blueprint
    from app import routes
    app.register_blueprint(routes.main_blueprint)

    return app