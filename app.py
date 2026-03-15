from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restx import Api
from config import Config

db = SQLAlchemy()
jwt = JWTManager()


def create_app(config_class=Config):
      app = Flask(__name__)
      app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)

    api = Api(
              app,
              version='1.0',
              title='Task Tracker API',
              description='A RESTful API for managing tasks',
              doc='/api/docs',
    )

    from routes.auth import auth_ns
    from routes.tasks import tasks_ns

    api.add_namespace(auth_ns, path='/api/auth')
    api.add_namespace(tasks_ns, path='/api/tasks')

    with app.app_context():
              db.create_all()

    return app


if __name__ == '__main__':
      app = create_app()
      app.run(debug=True, port=5000)
