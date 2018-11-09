import pathlib
import variable


class Mkdir():
    # def __init__(self, food_name, harmful):
    #     self.food_name = food_name
    #     self.harmful = harmful

    def save_path(self):
        old_json = variable.old_json
        if old_json['illegal_behavior'] == '超过食品安全标准限量的':
            save_path = (variable.path + '/' + old_json['company_name'] +
                         old_json['har'] + old_json['illegal_behavior'] +
                         old_json['food'] + '案')
        # return save_path
        else:
            save_path = (variable.path + '/' + old_json['company_name'] +
                         old_json['illegal_behavior'] + '案')
        pathlib.Path(save_path).mkdir(parents=True, exist_ok=True)
        return save_path


