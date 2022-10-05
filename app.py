from dbhelpers import conn_exe_close
import json
from flask import Flask

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
app.run(debug=True)