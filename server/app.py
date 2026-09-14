# Import Flask
from flask import Flask

# Create the Flask app instance
app = Flask(__name__)

# Car models currently in the fleet
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


# Handle GET requests to "/"
@app.route('/')
def index():
    # Return plain text as the response
    return 'Welcome to Flatiron Cars'