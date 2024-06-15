from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
  #  return 'Welcome to My First Flask Website!'
    return render_template('main/base.html')

@app.route('/event')
def event():
    return render_template('main/event.html')

@app.route('/estimate')
def estimate():
    return render_template('main/estimate.html')
    
 

if __name__ == '__main__':
#  app.run(host='127.0.0.1', port=5000)
    app.run(debug= True)
