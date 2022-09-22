#DEMO VERSION OF THE MAIN.py FILE TO UNDERSTAND THE FUNCTIONALITY OF THE FLASK FRAMEWORK...
from flask import Flask, render_template
from datetime import datetime

 app = Flask(__name__)

@app.route('/')
def hello():
    utc_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    return render_template("index.html", utc_time=utc_time)

if __name__=='__main__':
    app.run(debug=True)

    
#THE METHOD HELLO IS CALLING THE HTML CODE FILE THAT IS IN OUR STRUCTURE OF THE APPLICATION FILE.    
