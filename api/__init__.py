from flask import Flask
from api_place import app as place_app
from api_amenities import app as amenities_app
from api_country_city import app as country_city_app
from model.review import Review
from api_controller import app as api_app
from api_review import app as review_app

app = Flask(__name__)

app.register_blueprint(api_app)
app.register_blueprint(amenities_app)
app.register_blueprint(country_city_app)
app.register_blueprint(place_app)
app.register_blueprint(review_app)