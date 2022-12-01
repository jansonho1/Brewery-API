import pip._vendor.requests as requests
import json
from flask import Flask, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

data = requests.get("https://api.openbrewerydb.org/breweries")
state = {}
for brewery in data.json():
        thisState = brewery['state']
        if thisState not in state:
            state[thisState] = []
        breweryList = state[thisState]
        if brewery['name'] not in breweryList:
            breweryList.append(brewery['name'])
        state[thisState] = breweryList

@app.route("/")
def default():    
    return json.dumps(state)

@app.route("/table")
def format():
    initHTML = "<html><table><tr><th>State</th><th>Breweries</th></tr>"
    for curr in state:
        for brewery in state[curr]:
            if(curr != None and brewery != None):
                newRow = "<tr><td>" + curr + "</td><td>" + brewery + "</td></tr>"
                initHTML += newRow
    initHTML += "</table></html>"
    return initHTML


if __name__  == '__main__':
    app.run()
    