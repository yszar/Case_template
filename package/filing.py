import package.docxreplace
from package import changejson
from package import variable
from package import docxreplace
import package.changejson
import os
import pathlib


class Filing():
    path = os.path.dirname(__file__)
    alljson = variable.old_json

    # tempath = docxreplace.Docxreplace()
    # newpath = tempath.dirname

    # docxname = ""
    # link = ""

    def __init__(self, link, docxname, *food_har):
        self.docxname = docxname
        self.link = link
        self.food_har = food_har

    def go(self):
        # oldjson = package.docxreplace.docxreplace()
        # law_kay = oldjson["illegal_behavior"]
        temp_path = changejson.Changejson(self.food_har[0], self.food_har[1])
        save_path = temp_path.fullib(self.food_har[0], self.food_har[1])
        pathlib.Path(save_path).mkdir(parents=True, exist_ok=True)

        Docxreplace = docxreplace.Docxreplace()
        Docxreplace.replacedocx(self.link, self.docxname)
        if self.food_har:
            Changejson = changejson.Changejson(self.food_har[0],
                                               self.food_har[1])
        else:
            Changejson = changejson.Changejson()
        Changejson.changejson()


class Survey():
    def __init__(self, link, docxname, the_object):
        self.the_object = the_object
        self.docxname = docxname
        self.link = link

    def go(self):
        res = package.changejson.changejson(self.the_object)
        # package.docxreplace.fullib()
        package.docxreplace.replacedocx(self.link, self.docxname, res)
        changejson()


class Collegiate():
    path = os.path.dirname(__file__)
    alljson = variable.old_json

    # newpath = docxreplace.Docxreplace().dirname

    # docxname = ""
    # link = ""

    def __init__(self, link, docxname):
        self.docxname = docxname
        self.link = link

    # def __approval(self):
    #     doc = package.DocxTemplate(Filing.path + "/filing/2立案审批表.docx")
    #     # context = {'company_name': Filing.alljson['company_name']}
    #     doc.render(Filing.alljson)
    #     pathname = package.docxmkdir.pathname
    #     doc.save(pathname + '/2立案审批表.docx')

    def go(self):
        package.docxreplace.replacedocx(self.link, self.docxname)


class Inform():
    path = os.path.dirname(__file__)
    alljson = docxreplace.variable.old_json

    # newpath = docxreplace.Docxreplace().dirname

    # docxname = ""
    # link = ""

    def __init__(self, link, docxname):
        self.docxname = docxname
        self.link = link

    # def __approval(self):
    #     doc = package.DocxTemplate(Filing.path + "/filing/2立案审批表.docx")
    #     # context = {'company_name': Filing.alljson['company_name']}
    #     doc.render(Filing.alljson)
    #     pathname = package.docxmkdir.pathname
    #     doc.save(pathname + '/2立案审批表.docx')

    def go(self):
        package.docxreplace.replacedocx(self.link, self.docxname)


class Execution():
    path = os.path.dirname(__file__)
    alljson = docxreplace.variable.old_json

    # newpath = docxreplace.Docxreplace().dirname

    # docxname = ""
    # link = ""

    def __init__(self, link, docxname):
        self.docxname = docxname
        self.link = link

    # def __approval(self):
    #     doc = package.DocxTemplate(Filing.path + "/filing/2立案审批表.docx")
    #     # context = {'company_name': Filing.alljson['company_name']}
    #     doc.render(Filing.alljson)
    #     pathname = package.docxmkdir.pathname
    #     doc.save(pathname + '/2立案审批表.docx')

    def go(self):
        package.docxreplace.replacedocx(self.link, self.docxname)