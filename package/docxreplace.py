import os
import json
path = os.path.dirname(__file__)


def docxreplace():
    with open(path+'/information.json', 'r') as f:
        data = json.load(f)
    return data