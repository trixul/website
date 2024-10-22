from flask import Flask, render_template # Flask = object
app = Flask(__name__) # app = object of class                           Flask

@app.route("/") # decorator
def hello_world():
  return render_template('home.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
