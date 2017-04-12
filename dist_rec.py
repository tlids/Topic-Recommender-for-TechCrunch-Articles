import flask
from flask import request
import pandas as pd
import json


#---------- MODEL IN MEMORY ----------------#

# Recommend Topics Based on Input Topic and Closest Distance

#---------- URLS AND WEB PAGES -------------#

# Initialize the app
app = flask.Flask(__name__)

# Homepage

@app.route("/")
def viz_page():
    """
    Homepage: serve our visualization page, awesome.html
    """
    with open("recommend_mt.html", 'r') as viz_file:
        return viz_file.read()

# Get an input and display response for the recommendations
@app.route("/rec", methods=["POST"])
def recommender():
    """
    When A POST request with json data is made to this uri,
    Read the example from the json, make recommendations and
    send it with a response
    """
    # Get recommendations for our example that came with the request
    

    tag = request.json['rec']
    
    df = pd.read_pickle('dist_df.pkl')
    d = dict(df[tag])
    sorted_dist = sorted(d.items(), key=lambda x: x[1])
    
    results = {"recommendation": ['1: ', sorted_dist[1][0], ', 2: ', sorted_dist[2][0], ', 3: ', sorted_dist[3][0]]}
    return flask.jsonify(results)

#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
# app.run(host='0.0.0.0')
app.run(debug=True)
