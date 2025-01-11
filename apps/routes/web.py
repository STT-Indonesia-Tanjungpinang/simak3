from flask import Blueprint
from apps.controllers.FrontendController import frontend_index
from apps.controllers.AuthController import auth_login

web_route = Blueprint('blueprint', __name__)

web_route.route('/', methods=['GET'])(frontend_index)
# frontend - Login
web_route.route('/', methods=['GET'])(frontend_index)
web_route.route('/login', methods=['GET'])(auth_login)


# https://github.com/Syed007Hassan/Flask-MVC-Template-/blob/main/src/controllers/reorderController.py