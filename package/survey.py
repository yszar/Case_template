import package.docxreplace


class Survey():
    def __init__(self, link, docxname, the_object):
        self.the_object = the_object
        self.docxname = docxname
        self.link = link

    def go(self):
        package.docxreplace.replacedocx(self.link, self.docxname,
                                        self.changejson(self.the_object))
