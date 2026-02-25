from flask import Flask,render_template,request,redirect,url_for
from models.notice import db, Notice
from routes.notice_routes import notice_bp
import os

def create_app():
    app=Flask(__name__)

    #DB Config
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "fallback-secret")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///database.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    app.register_blueprint(notice_bp, url_prefix="/notices")

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app=create_app()
    app.run()