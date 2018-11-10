from package import filing

hearing = filing.Inform('22听证告知书')
hearing.go()

advance_notice = filing.Inform('26行政处罚事先告知书')
advance_notice.go()

receipt = filing.Inform('38事先告知送达回执')
receipt.go()
