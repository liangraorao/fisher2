from flask import Flask
from app.models.base import db
from flask_login import LoginManager


login_manage = LoginManager()


def create_app():
    app = Flask(__name__)
    # 注意配置文件路径
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    login_manage.init_app(app)
    login_manage.login_view = 'web.login'
    login_manage.login_message = '请先登录或注册'
    db.create_all(app=app)
    # with app.app_context():
    #     db.create_all()
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)