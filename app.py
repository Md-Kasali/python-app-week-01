from flask import Flask, render_template
import os

# Issue 1: Hardcoded absolute path that may not work on all Linux systems
app = Flask(__name__, template_folder='/home/user/templates')

# Issue 2: Trying to access environment variable without checking if it exists
SECRET_KEY = os.environ['SECRET_KEY']

@app.route('/')
def index():
    """Display the static page."""
    return render_template('index.html')

if __name__ == '__main__':
    # Issue 3: Port might be already in use, no error handling
    app.run(debug=True, host='0.0.0.0', port=5000)

