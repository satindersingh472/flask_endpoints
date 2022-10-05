from dbhelpers import conn_exe_close
import json
from flask import Flask, request

app = Flask(__name__)

@app.get('/api/clients')
def all_users():
    results = conn_exe_close('call all_users()',[])
    if(type(results) == list):
        results_json = json.dumps(results,default=str)
        return results_json
    else:
        return 'Sorry, something went wrong'

# all_users()

@app.get('/api/loyal/clients')
def loyal_clients():
    min_points = request.args.get('min_points')
    results = conn_exe_close('call min_points(?)',[min_points])
    if(type(results) == list):
        results_json = json.dumps(results,default=str)
        return results_json
    else:
        return 'Sorry, something went wrong'


app.run(debug=True)