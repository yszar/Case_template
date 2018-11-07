from package import filing

source = filing.Filing('filing', '1案件来源登记表')
# source.link = "filing"
# source.docxname = "1案件来源登记表"
source.replacedocx()

approval = filing.Filing('filing', '2立案审批表')
# approval.link = "filing"
# approval.docxname = "2立案审批表"
approval.replacedocx()