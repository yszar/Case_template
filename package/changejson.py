# import package.docxreplace
import json
import time
import os

# def dictget(dict1, obj, default=None):
#     for k, v in dict1.items():
#         if k == obj:
#             print(v)
#         else:
#             if type(v) is dict:
#                 re = dictget(v, obj)
#                 if re is not default:
#                     print(re)


def get_dict_value(date, keys, default=None):
    # default=None，在key值不存在的情况下，返回None
    keys_list = keys.split('.')
    # 以“.”为间隔，将字符串分裂为多个字符串，其实字符串为字典的键，保存在列表keys_list里
    if isinstance(date, dict):
        # 如果传入的数据为字典
        dictionary = dict(date)
        # 初始化字典
        for i in keys_list:
            # 按照keys_list顺序循环键值
            try:
                if dictionary.get(i) != None:
                    dict_values = dictionary.get(i)
                # 如果键对应的值不为空，返回对应的值
                elif dictionary.get(i) == None:
                    dict_values = dictionary.get(int(i))
                # 如果键对应的值为空，将字符串型的键转换为整数型，返回对应的值
            except:
                return default
                # 如果字符串型的键转换整数型错误，返回None
            dictionary = dict_values
        return dictionary
    else:
        # 如果传入的数据为非字典
        try:
            dictionary = dict(eval(date))
            # 如果传入的字符串数据格式为字典格式，转字典类型，不然返回None
            if isinstance(dictionary, dict):
                for i in keys_list:
                    # 按照keys_list顺序循环键值
                    try:
                        if dictionary.get(i) != None:
                            dict_values = dictionary.get(i)
                        # 如果键对应的值不为空，返回对应的值
                        elif dictionary.get(i) == None:
                            dict_values = dictionary.get(int(i))
                        # 如果键对应的值为空，将字符串型的键转换为整数型，返回对应的值
                    except:
                        return default
                        # 如果字符串型的键转换整数型错误，返回None
                    dictionary = dict_values
                return dictionary
        except:
            return default


# if the_json['illegal_behavior'] == '超过食品安全标准限量的':
#     print('输入超限食品名称')
#     food_name = input()
#     print('输入超限的元素')
#     harmful = input()
#     the_json['illegal_behavior'] = harmful + '超过食品安全标准限量的' + food_name
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def docxreplace():
    with open(path + '/information.json', 'r') as f:
        data = json.load(f)
    return data


the_json = docxreplace()


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


# def law_json():
#     pass