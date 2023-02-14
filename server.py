from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say_name(name):
    return f"Hello {name}!"

@app.route('/repeat/<int:num>/<string:name>')
def repeat_name(num, name):
    return f"{name * num}"

@app.route('/<path:path>')
def catch_all(path):
    return f"Sorry! {path} had no response. Try again."

if __name__=="__main__":   
    app.run(debug=True, port=5000) 