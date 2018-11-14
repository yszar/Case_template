# import json
import time
# from package import variable
from package import judge

# from package import get_dict_value

# import pathlib

# class Changejson():

#     old_json = variable.old_json

#     def __init__(self, food_name, harmful):
#         self.food_name = food_name
#         self.harmful = harmful


def age(number):
    current = int(time.strftime("%Y"))
    year = int(number[6:10])
    age = current - year
    return age


def changejson(new_json, *the_object):
    # json = package.docxreplace.package.docxreplace()

    if the_object == '2':
        print('输入授权委托人职务')
        position = input()
        print('输入授权委托人姓名')
        name = input()
        print('输入授权委托人身份证号码')
        idnum = input()
        new_json['legal_representative'] = name
        new_json['identification_number'] = idnum
        new_json['position'] = position
    finally_id = new_json['identification_number']
    if int(finally_id[-2]) % 2 == 0:
        new_json['gender'] = '女'
    else:
        new_json['gender'] = '男'
    new_json['age'] = str(age(new_json['identification_number']))

    if new_json['category'] == '食':
        new_json['business'] = '食品经营'
        new_json['law_name'] = '《中华人民共和国食品安全法》'
        # Changejson.law_json('shi')
        if judge.judge() == 'overrun':
            new_json['illegal_behavior'] = (
                new_json['har'] + new_json['illegal_behavior'] +
                new_json['food'])
    elif new_json['category'] == '药':
        new_json['business'] = '药品经营'
    elif new_json['category'] == '妆':
        new_json['business'] = '化妆品经营'
    elif new_json['category'] == '械':
        new_json['business'] = '医疗器械经营'
    # if new_json['illegal_behavior'] == '超过食品安全标准限量的':
    #     print('输入超限食品名称')
    #     food_name = input()
    #     print('输入超限的元素')
    #     harmful = input()
    #     new_json['fullib'] = harmful + '超过食品安全标准限量的' + food_name
    return new_json
