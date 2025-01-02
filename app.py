from flask import Flask

from api.routes import api
from sites.routes import site

app = Flask(__name__)

app.register_blueprint(api)
app.register_blueprint(site)

if __name__ == '__main__':
  app.run(debug = True)