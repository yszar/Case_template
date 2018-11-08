import os
import json

path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def docxreplace():
    with open(path + '/information.json', 'r') as f:
        data = json.load(f)
    return data


old_json = docxreplace()

save_path = ''