
from flask import Flask, request, Response, render_template, jsonify
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# CORS(app, supports_credentials=True)
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route("/getHouseMap", methods=["POST","GET"])
@cross_origin()
def getHouseMap():
    data = request.get_data()
    response = Response()
    
    response_json = {
            "type": "FeatureCollection",
            "features": [
                {
                "type": "Feature",
                "id":"01",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [0, 0],
                        [10, 0],
                        [10, 7],
                        [5, 7],
                        [5, 4],
                        [0, 4],
                        [0, 0]
                    ]
                    ]
                },
                "properties": {
                    "name": "House"
                }
                },
                {
                "type": "Feature",
                "id":"02",
                "properties": {
                    "name": "Table"
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [2, 2],
                        [6, 2],
                        [6, 3],
                        [2, 3],
                        [2, 2]
                    ]
                    ]
                }
                }

            ]
            }

    
    response.data=json.dumps(response_json)
    return response

@app.route("/getPeoplePose", methods=["POST","GET"])
@cross_origin()
def getPeoplePose():
    data = request.get_data()
    response = Response()
    
    response_json = [
            [0.5, 0.5, 1],
            [0.6, 0.5, 1],
            [0.7, 0.5, 1],
            [0.8, 0.5, 1],
            [0.9, 0.5, 1]
        ]
    
    response.data=json.dumps(response_json)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="7000",debug=True)