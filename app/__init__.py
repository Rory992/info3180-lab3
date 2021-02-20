from flask import Flask
from flask_mail import Mail
from .config import Config
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()

app = Flask(__name__)
#app.config.from_object(Config)

app.config['SECRET_KEY'] = 'happy'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = '430f64218db983'
app.config['MAIL_PASSWORD'] = '2e4e64b9dde025'

mail = Mail(app)
csrf.init_app(app)
from app import views