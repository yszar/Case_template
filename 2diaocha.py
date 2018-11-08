from package import survey

print('负责人本人输入1，授权委托人输入2')
the_object = input()

record = survey.Survey('survey', '7询问调查笔录', the_object)
record.go()

report = survey.Survey('survey', '9案件调查终结报告', the_object)
report.go()