from flask import Flask
import os
import redis # in memory caching
import time

import redis.exceptions


app = Flask(__name__)

cache = redis.Redis(host='redis', port = 6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            cache.reset_retry_count()
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries==0:
                raise exc
            retries-=1
            
@app.route('/')
def hello():
    count = get_hit_count()
    return ' hesham i have seen {} times. \n'.format(count)


# @app.route('/', methods = ['GET'])

# def home():
#     return "welcome back hesham"



# if __name__=="__main__":
#     app.run(debug = True,
#             host= "0.0.0.0", port=5001)  
#     # bcs of 0.0.0.0 we cna run with localhost and 127. as well
    
    