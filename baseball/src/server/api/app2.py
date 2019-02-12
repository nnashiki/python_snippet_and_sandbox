import numpy as np
from bokeh.models import AjaxDataSource, CustomJS
from bokeh.plotting import figure, show
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


x = list(np.arange(0, 6, 0.1))
y = list(np.sin(x) + np.random.random(len(x)))


@app.route('/data', methods=['GET', 'OPTIONS', 'POST'])
@crossdomain
def data():
    x.append(x[-1] + 0.1)
    y.append(np.sin(x[-1]) + np.random.random())
    return jsonify(points=list(zip(x, y)))



if __name__ == '__main__':
    app.run(port=5050, host="0.0.0.0")
