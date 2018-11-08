from package import inform

hearing = inform.Inform('inform', '22听证告知书')
# source.link = "filing"
# source.docxname = "1案件来源登记表"
hearing.go()

advance_notice = inform.Inform('inform', '26行政处罚事先告知书')
advance_notice.go()

receipt = inform.Inform('inform', '38事先告知送达回执')
receipt.go()
