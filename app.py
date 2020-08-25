from flask import Flask
from new_magic_formula.model import Recommendation_Stock_Model
import json
from flask_cors import CORS

app = Flask(__name__)


@app.route('/recommendation/<period>/<propensity>', methods=['GET'])
def recommend_stock(period, propensity):
    period = period
    propensity = propensity
    print(period, propensity)
    recommend_stock_model = Recommendation_Stock_Model()
    return json.dumps(recommend_stock_model.recommendation_listing(period=period, propensity=propensity))


CORS(app)
if __name__ == '__main__':
    app.run()
