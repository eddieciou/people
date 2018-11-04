from flask import Flask,render_template
from flask_restful_swagger_2 import Api
from flask_cors import CORS
from net.route.PeopleApi import *
# Create the application instance
app = Flask(__name__)
CORS(app)
api = Api(app, api_version='0.0', api_spec_url='/api/swagger')




# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


api.add_resource(GetPelple, '/api/people')


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)