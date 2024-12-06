from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager

db = SQLAlchemy()
DB_NAME = 'database_sqlite3'

def create_database():
    db.create_all()
    print('Database created!')

# initialize app
def create_app():
    app = Flask(__name__)
    # encrypting session data
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    login_manager = LoginManager() # keep track of user sessions and access tokens
    login_manager.init_app(app) # initialize login manager
    login_manager.login_view = 'auth.login' # redirect to login page if user is not logged in

    @login_manager.user_loader
    def load_user(id):
        return Customer.query.get(int(id))

    # register blueprints
    from .views import views
    from .auth import auth
    from .admin import admin
    from .models import Customer, Cart, Product, Order

    app.register_blueprint(views, url_prefix='/') # localhost:5500/about-us
    app.register_blueprint(auth, url_prefix='/') # localhost:5500/auth/change-password
    app.register_blueprint(admin, url_prefix='/')

    with app.app_context():
        create_database()
        
    return app
