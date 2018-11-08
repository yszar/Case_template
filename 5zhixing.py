from package import execution

approval = execution.Execution('execution', '27行政处罚决定审批表')
# source.link = "filing"
# source.docxname = "1案件来源登记表"
approval.go()

penalty_decision = execution.Execution('execution', '28行政处罚决定书')
penalty_decision.go()

receipt = execution.Execution('execution', '38送达回执')
receipt.go()

closing_case = execution.Execution('execution', '40行政处罚结案报告')
closing_case.go()

print('是否有没收物品？（Y/N）')
confiscation = input()

if confiscation.lower() == 'y':
    certificate = execution.Execution('execution', '30没收物品凭证')
    certificate.go()
    confiscation_list = execution.Execution('execution', r'37(没收)物品清单')
    confiscation_list.go()
    processing_list = execution.Execution('execution', '31没收物品处理清单')
    processing_list.go()


