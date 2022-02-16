# python3

import json

def config():
    with open("config.json") as fp:
        data  = json.load(fp)
    return data