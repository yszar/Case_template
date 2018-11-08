import package.docxreplace


class Survey():
    def __init__(self, link, docxname, the_object):
        self.the_object = the_object
        self.docxname = docxname
        self.link = link

    def changejson(self):
        if self.the_object == '2':
            print('输入授权委托人职务')
            position = input()
            json = package.docxreplace.docxreplace()
            json['legal_representative'] = '张无忌'
            json['identification_number'] = '620102198702120001'
            json['position'] = position
            if json['category'] == '食':
                json['business'] = '食品经营'
            elif json['category'] == '药':
                json['business'] = '药品经营'
            elif json['category'] == '妆':
                json['business'] = '化妆品经营'
            elif json['category'] == '械':
                json['business'] = '医疗器械经营'
            return json
        if self.the_object == "1":
            return package.docxreplace.docxreplace()

    def go(self):
        package.docxreplace.replacedocx(self.link, self.docxname, self.changejson())
