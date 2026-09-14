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

# Handle GET requests to "/<model>"
@app.route('/<model>')
def get_model(model):
    # Check if requested model exists in fleet
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'