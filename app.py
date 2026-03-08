from flask import Flask, redirect, url_for,render_template
from models.notice import db
from routes.notice_routes import notice_bp
from config import Config
from extensions import db, migrate, bcrypt, api, cors

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load config from config.py

    db.init_app(app)
    migrate.init_app(app,db)
    bcrypt.init_app(app)
    api.init_app(app)
    cors.init_app(app)

    app.register_blueprint(notice_bp, url_prefix="/notices")

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return render_template('data_teal.html')

    return app

if __name__ == "__main__":
    app=create_app()
    app.run(debug=True)