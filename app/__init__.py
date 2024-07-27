from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from config import SECRET_KEY

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
    )
    bootstrap.init_app(app)

    from app.routes.courses_route import courses
    app.register_blueprint(courses)

    return app