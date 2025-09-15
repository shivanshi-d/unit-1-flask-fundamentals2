from flask import Flask

app = Flask(__name__)

@app.route('/') # / Front Door (home page)
def home(): #Function name (can be anything)
    return "home page" # What visitors see

@app.route('/about')
def about():
    # return "about page"
    return """
    <h1>Welcome</h1>
    <p> This is my first website </p>
    """

@app.route('/contact')
def contact():
    return "contact page"


app.run(debug=True)