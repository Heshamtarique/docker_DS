from flask import Flask
import os

app = Flask(__name__)


@app.route('/', methods = ['GET'])

def home():
    return "welcome back hesham"



if __name__=="__main__":
    app.run(debug = True,
            host= "0.0.0.0", port=5001)  
    # bcs of 0.0.0.0 we cna run with localhost and 127. as well
    