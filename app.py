from flask import Flask # Flask = object
app = Flask(__name__) # app = object of class                           Flask

@app.route("/") # decorator
def hello_world():
  return("Hello Trisha")

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
