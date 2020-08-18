from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        subscriptionKey = "552ec13295374a19ba642f20be41537a"
        customConfigId = "6f849a36-021c-4da0-a12a-353ff20f493b"
        searchTerm = request.form['input']

        url = 'https://api.cognitive.microsoft.com/bingcustomsearch/v7.0/search?' + \
            'q=' + searchTerm + '&' + 'customconfig=' + customConfigId

        response = requests.get(
            url, headers={'Ocp-Apim-Subscription-Key': subscriptionKey})

        cardata = json.loads(response.text)
        search_response = cardata['webPages']['value']
        return render_template("index.html", values=search_response)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
