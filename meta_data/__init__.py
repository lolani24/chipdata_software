def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "zxcvbnm"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
