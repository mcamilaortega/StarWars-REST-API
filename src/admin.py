# admin.py
import os
from flask_admin import Admin
from models import db, User, Planets, Characters, Favorite  # Corrected model name from 'Favorites' to 'Favorite'
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    # Add models to admin view
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Planets, db.session))
    admin.add_view(ModelView(Characters, db.session))
    admin.add_view(ModelView(Favorite, db.session))  