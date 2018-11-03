from flask import Flask

def create_app():
    app = Flask(__name__)
    # 注意配置文件路径
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
