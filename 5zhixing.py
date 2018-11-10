from package import filing

approval = filing.Execution('27行政处罚决定审批表')
approval.go()

penalty_decision = filing.Execution('28行政处罚决定书')
penalty_decision.go()

receipt = filing.Execution('38决定书送达回执')
receipt.go()

closing_case = filing.Execution('40行政处罚结案报告')
closing_case.go()

print('是否有没收物品？（Y/N）')
confiscation = input()

if confiscation.lower() == 'y':
    certificate = filing.Execution('30没收物品凭证')
    certificate.go()
    confiscation_list = filing.Execution(r'37(没收)物品清单')
    confiscation_list.go()
    processing_list = filing.Execution('31没收物品处理清单')
    processing_list.go()




