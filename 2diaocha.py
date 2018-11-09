from package import filing
# import package.docxreplace
print('本人输入1，授权委托人输入2')
ren = input()
if ren == '1':
    record = filing.Survey('7询问调查笔录')
    record.go()
if ren == '2':
    print('输入授权委托人姓名')
    name = input()
    print('输入授权委托人身份证号码')
    id_num = input()
    # Survey.old_json['legal_representative'] = name
    # Survey.old_json['identification_number'] = id_num
    record = filing.Survey('7询问调查笔录', name, id_num)
    record.go()

report = filing.Survey('9案件调查终结报告')

report.go()
