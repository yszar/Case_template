from package import variable
from package import get_dict_value
import json
import pinyin
old_json = variable.docxreplace()


def lawopen(txt):
    # path = package.docxreplace.path
    with open(variable.path + txt, 'r') as f:
        data = json.load(f)
    return data


def law_json(name):
    name = pinyin.get(name, format="strip", delimiter=" ")
    law = lawopen("/law/" + name + ".json")

    old_json['violation'] = get_dict_value.get_dict_value(
        law, old_json['illegal_behavior'] + ".violation")
    old_json['violation_content'] = get_dict_value.get_dict_value(
        law, old_json['illegal_behavior'] + ".violation_content")
    old_json['according'] = get_dict_value.get_dict_value(
        law, old_json['illegal_behavior'] + ".according")
    old_json['according_content'] = get_dict_value.get_dict_value(
        law, old_json['illegal_behavior'] + ".according_content")
    return old_json
