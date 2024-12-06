from flask import Blueprint, render_template

# routes or url endpoints
views = Blueprint('views', __name__)

# decorator to build a function to a url endpoint
@views.route('/')
def home():
    return render_template('index.html')