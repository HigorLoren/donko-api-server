from flask import Flask, request
from flask_cors import CORS

from src.endpoints.blueprint_user import blueprint_user

app = Flask(__name__, static_url_path='', static_folder='static')
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# register blueprints. ensure that all paths are versioned!
app.register_blueprint(blueprint_user, url_prefix="/api/v1/user")

@app.route('/health', methods=['GET','POST'])
def index():
  if request.method == 'POST':
    #check user details from db
    return 'Server Works with POST!'
  elif request.method == 'GET':
    return 'Server Works with GET!'
