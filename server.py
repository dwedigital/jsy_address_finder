from flask import Flask, Response, request
import requests
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/',methods=['POST'])
def proxy():
    if request.method == 'POST':

        data = request.get_json()
        query = data['query']
        payload = {'query': query}
        payload = json.dumps(payload)
        headers = {
        'Content-Type': 'application/json',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        }
        resp = requests.post('https://us-central1-fetch-serverless.cloudfunctions.net/addressLookup ', data=payload, headers=headers)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in     resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response

if __name__ == '__main__':
    app.run()