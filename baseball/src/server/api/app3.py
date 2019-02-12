import numpy as np
from flask import Flask, jsonify, make_response, request

# Bokeh related code


# Flask related code

app = Flask(__name__)


def crossdomain(f):
    def wrapped_function(*args, **kwargs):
        resp = make_response(f(*args, **kwargs))
        h = resp.headers
        h['Access-Control-Allow-Origin'] = '*'
        h['Access-Control-Allow-Methods'] = "GET, OPTIONS, POST"
        h['Access-Control-Max-Age'] = str(21600)
        requested_headers = request.headers.get('Access-Control-Request-Headers')
        if requested_headers:
            h['Access-Control-Allow-Headers'] = requested_headers
        return resp

    return wrapped_function


x = []
y = []


@app.route('/data2', methods=['GET', 'OPTIONS', 'POST'])
@crossdomain
def data():
    x = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,2016, 2017, 2018]
    y = [26, 10, 33, 24, 32, 44, 20, 27, 32, 19, 15, 12, 15, 11]
    return jsonify(points=list(zip(x, y)))



if __name__ == '__main__':
    app.run(port=5050, host="0.0.0.0")
