import pathlib
from package import variable
from package import judge

# class Mkdir():
#     # def __init__(self, food_name, harmful):
#     #     self.food_name = food_name
#     #     self.harmful = harmful


def save_path():
    old_json = variable.docxreplace()
    if judge.judge() == 'overrun':
        save_path = (
            variable.path + '/' + old_json['company_name'] + old_json['har'] +
            old_json['illegal_behavior'] + old_json['food'] + '案')
    # return save_path
    elif judge.judge() == 'noverrun':
        save_path = (variable.path + '/' + old_json['company_name'] +
                     old_json['illegal_behavior'] + '案')
    pathlib.Path(save_path).mkdir(parents=True, exist_ok=True)
    return save_path
