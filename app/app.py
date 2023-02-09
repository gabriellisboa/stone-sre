import random
import logging

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', filename='/var/log/app/app.log', filemode='w', level=logging.DEBUG)

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def index():
    number = random.randint(0, 500)
    logging.info('random number is %s', number)
    return '{"status": "200", "number": %s}'%(number)

@app.errorhandler(404)
def page_not_found(e):
    # app.logger.error('%s', e)
    logging.error('{"status": "404"}')
    return '{"status": "404"}'

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0")
