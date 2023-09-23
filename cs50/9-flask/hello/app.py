from flask import Flask, render_template, request

# Note: __name__ refers current file, passing the file to constructor call, creating an application object.
app = Flask(__name__)

names = []



# Decorator, the function below will be called everytime the user made a HTTP request(default is GET) to the server with URL not containing an actual route, ie: www.domain.com/
@app.route('/')
def index():
# The render_template mothod returns the file(name equals to the param) inside the 'templates' directory.
    return render_template('index.html')



@app.route('/greet')
def greet():
# get method returns the value of the key:value pair(passing in the key as param) in the URL. For eg. the URL keyed into the browser can be: www.example.com/route/?name=value
# Second param is the default value.
    name = request.args.get('name', 'world')
    # Make sure to do *server-side validation* of data! html code can be easily changed by using inspect function on the browser. For example:
    if not name:
        return render_template('failure.html')
    names.append(name)
# It can take in multiple params in key:value pairs. 'placeholder' is the named variable created in html file as such: {{ placeholder }}, the variable can then be replaced accordingly.
    return render_template('greet.html', placeholder=name)



# To see a list of responses from the form:

@app.route('/greeted')
def greeted():
    # The param should be the named iterable inside the for iteration of the html tag, setting it to the iterables created here.
    return render_template('greeted.html', list=names)



# flask provides a Session class, which can implement a Log-In Session and Set-Cookie functionality, in which each session object is created specific to each User.