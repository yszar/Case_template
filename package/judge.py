from package import variable


def judge():
    old_json = variable.docxreplace()

    if '超过食品安全标准限量的' in old_json['illegal_behavior']:
        # save_path = (
        #     variable.path + '/' + old_json['company_name'] + old_json['har'] +
        #     old_json['illegal_behavior'] + old_json['food'] + '案')
        # illegal_behavior = (
        #     old_json['har'] + old_json['illegal_behavior'] + old_json['food'])
        return 'overrun'
    else:
        return 'noverrun'
        # save_path = (variable.path + '/' + old_json['company_name'] +
        #              old_json['illegal_behavior'] + '案')
        # illegal_behavior = old_json['illegal_behavior']
    # return save_path, illegal_behavior
