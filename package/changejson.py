# import package.test
import json
import time
import os
from package import variable


class changejson():

    the_json = variable.old_json

    def lawopen(txt):
        # path = package.docxreplace.path
        with open(path + txt, 'r') as f:
            data = json.load(f)
        return data

    def law_json(name):
        law_name = lawopen("/law/" + name + ".json")

        the_json['violation'] = get_dict_value(
            law_name, the_json['illegal_behavior'] + ".violation")
        the_json['violation_content'] = get_dict_value(
            law_name, the_json['illegal_behavior'] + ".violation_content")
        the_json['according'] = get_dict_value(
            law_name, the_json['illegal_behavior'] + ".according")
        the_json['according_content'] = get_dict_value(
            law_name, the_json['illegal_behavior'] + ".according_content")

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
            the_json['legal_representative'] = name
            the_json['identification_number'] = idnum
            the_json['position'] = position

        the_json['age'] = str(age(the_json['identification_number']))

        the_json['illegal_behavior'] = ''

        if the_json['category'] == '食':
            the_json['business'] = '食品经营'
            the_json['law_name'] = '《中华人民共和国食品安全法》'
            law_json('shi')
        elif the_json['category'] == '药':
            the_json['business'] = '药品经营'
        elif the_json['category'] == '妆':
            the_json['business'] = '化妆品经营'
        elif the_json['category'] == '械':
            the_json['business'] = '医疗器械经营'
        # if the_json['illegal_behavior'] == '超过食品安全标准限量的':
        #     print('输入超限食品名称')
        #     food_name = input()
        #     print('输入超限的元素')
        #     harmful = input()
        #     the_json['fullib'] = harmful + '超过食品安全标准限量的' + food_name
        return the_json
