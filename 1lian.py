from package import filing
# import package.docxreplace

source = filing.Filing('1案件来源登记表')

source.go()

approval = filing.Filing('2立案审批表')

approval.go()
