import os
from flask import Flask
from apps.routes.web import web_route

def create_app():
  # template_dir = os.path.abspath('../../src/views')

  app = Flask(__name__)  # flask app object

  # register blueprint
  app.register_blueprint(web_route, url_prefix='/')
  return app

app = create_app()  

if __name__ == '__main__':  # Running the app
  app.run(host='127.0.0.1', port=5000, debug=True)