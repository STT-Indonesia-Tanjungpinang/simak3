from flask import Blueprint

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
def getdata():
  data = {
    'key': 'value'
  }
  return data