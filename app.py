from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def index():
    """Return Homepage"""

    search_term = request.args.get('search_term')
  # TODO: Make 'params' dictionary containing:
  # a) the query term, 'q'
  # b) your API key, 'key'
  # c) how many GIFs to return, 'limit'
    params = {"q": search_term, "key": "UKFHT9WVVN4O", "limit": 10}
    r = requests.get("https://api.tenor.com/v1/search", params = params)
    gifs = r.json()["results"]
    print (r.json())
   # TODO: Using dictionary notation, get the 'results' field of the JSON,
   # which contains the GIFs as a list
   # TODO: Render the 'index.html' template, passing the list of gifs as a
   # named parameter called 'gifs'
    gifs = json.loads(r.content)['results']
    return render_template("index.html", gifs=gifs)




if __name__ == '__main__':
   app.run(debug=True)
