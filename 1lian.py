from package import filing
# import package.docxreplace


source = filing.Filing('filing', '1案件来源登记表', '粉条', '经营铝的残留量')
# package.docxreplace.fullib('粉条', '经营铝的残留量')

# source.link = "filing"
# source.docxname = "1案件来源登记表"
source.go()

approval = filing.Filing('filing', '1案件来源登记表', '粉条', '经营铝的残留量')
# package.docxreplace.fullib('粉条', '经营铝的残留量')
# approval.link = "filing"
# approval.docxname = "2立案审批表"
approval.go()