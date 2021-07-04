from discord.enums import Status
import flask
import requests
import json
from flask import request, jsonify
from bs4 import BeautifulSoup

app = flask.Flask(__name__)
app.config["DEBUG"] = True
#app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['GET'])
def index():
    return "[GET] /lastest"

@app.route('/lastest', methods=['GET'])
def api():
    url = "https://xn--42cah7d0cxcvbbb9x.com/"
    r = requests.get(url)
    soupObject = BeautifulSoup(r.text, "html.parser")
    table = soupObject.find_all('td', class_="em bg-em g-n")
    date = soupObject.find('td',class_="span bg-span txtd al-r")
    time = soupObject.find('td', class_ = "em bg-span txtd al-r")

    gold_bar_buy = table[0]
    gold_bar_sell = table[1]
    gold_jewelry_buy = table[2]
    gold_jewelry_sell = table[3]

    date = date.contents[0]
    time = time.contents[0]
    gold_bar_buy = gold_bar_buy.contents[0]
    gold_bar_sell = gold_bar_sell.contents[0]
    gold_jewelry_buy = gold_jewelry_buy.contents[0]
    gold_jewelry_sell = gold_jewelry_sell.contents[0]

    data = {"status":"success",
                "response":{"date":date, 
                            "update_time":time,
                            "price": {
                                "gold": {
                                    "buy":gold_jewelry_buy,
                                    "sell":gold_jewelry_sell
                                    },
                                "gold_bar": {
                                    "buy":gold_bar_buy,
                                    "sell":gold_bar_sell
                                    }, 
                                },
                            },
                        }   

    return json.dumps(data,ensure_ascii=False)

app.run()
