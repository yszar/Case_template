import json
import time
from package import variable
from package import get_dict_value

# import pathlib


class Changejson():

    old_json = variable.old_json

    def __init__(self, food_name, harmful):
        self.food_name = food_name
        self.harmful = harmful

    def lawopen(txt):
        # path = package.docxreplace.path
        with open(variable.path + txt, 'r') as f:
            data = json.load(f)
        return data

    def law_json(name):
        law_name = Changejson.lawopen("/law/" + name + ".json")

        Changejson.old_json['violation'] = get_dict_value.get_dict_value(
            law_name, Changejson.old_json['illegal_behavior'] + ".violation")
        Changejson.old_json[
            'violation_content'] = get_dict_value.get_dict_value(
                law_name,
                Changejson.old_json['illegal_behavior'] + ".violation_content")
        Changejson.old_json['according'] = get_dict_value.get_dict_value(
            law_name, Changejson.old_json['illegal_behavior'] + ".according")
        Changejson.old_json[
            'according_content'] = get_dict_value.get_dict_value(
                law_name,
                Changejson.old_json['illegal_behavior'] + ".according_content")

    def age(number):
        current = int(time.strftime("%Y"))
        year = int(number[6:10])
        age = current - year
        return age

    
    def changejson(*the_object):
        # json = package.docxreplace.package.docxreplace()

        if the_object == '2':
            print('输入授权委托人职务')
            position = input()
            print('输入授权委托人姓名')
            name = input()
            print('输入授权委托人身份证号码')
            idnum = input()
            Changejson.old_json['legal_representative'] = name
            Changejson.old_json['identification_number'] = idnum
            Changejson.old_json['position'] = position

        Changejson.old_json['age'] = str(
            Changejson.age(Changejson.old_json['identification_number']))

        Changejson.old_json['illegal_behavior'] = ''

        if Changejson.old_json['category'] == '食':
            Changejson.old_json['business'] = '食品经营'
            Changejson.old_json['law_name'] = '《中华人民共和国食品安全法》'
            Changejson.law_json('shi')
        elif Changejson.old_json['category'] == '药':
            Changejson.old_json['business'] = '药品经营'
        elif Changejson.old_json['category'] == '妆':
            Changejson.old_json['business'] = '化妆品经营'
        elif Changejson.old_json['category'] == '械':
            Changejson.old_json['business'] = '医疗器械经营'
        # if Changejson.old_json['illegal_behavior'] == '超过食品安全标准限量的':
        #     print('输入超限食品名称')
        #     food_name = input()
        #     print('输入超限的元素')
        #     harmful = input()
        #     Changejson.old_json['fullib'] = harmful + '超过食品安全标准限量的' + food_name
        return Changejson.old_json
