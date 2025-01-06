from flask import Blueprint
from apps.controllers.FrontendController import frontend_index

web_route = Blueprint('blueprint', __name__)

web_route.route('/', methods=['GET'])(frontend_index)


# https://github.com/Syed007Hassan/Flask-MVC-Template-/blob/main/src/controllers/reorderController.py