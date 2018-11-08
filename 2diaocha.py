from package import survey
import package.docxreplace


print('负责人本人输入1，授权委托人输入2')
the_object = input()

record = survey.Survey('survey', '7询问调查笔录', the_object)
package.docxreplace.fullib('粉条', '经营铝的残留量')
record.go()

report = survey.Survey('survey', '9案件调查终结报告', the_object)
package.docxreplace.fullib('粉条', '经营铝的残留量')
report.go()