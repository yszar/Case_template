import package.docxreplace
from package import changejson
from package import variable
from package import docxreplace
from package import loadlaw
from package import mkdir
import package.changejson
import os


class Filing():
    path = os.path.dirname(__file__)

    old_json = variable.docxreplace()

    def __init__(self, docxname):
        self.docxname = docxname

    def go(self):
        # json中增加违反和依据的法律内容
        save_path = mkdir.save_path()
        law_name = Filing.old_json['category']
        if Filing.old_json['violation'] == "":
            Filing.old_json = loadlaw.law_json(law_name)
        new_json = changejson.changejson(Filing.old_json)
        docxreplace.replacedocx(save_path, self.docxname, new_json)


class Survey():
    # def __init__(self, link, docxname, the_object):
    #     self.the_object = the_object
    #     self.docxname = docxname
    #     self.link = link

    # def go(self):
    #     res = package.changejson.changejson(self.the_object)
    #     # package.docxreplace.fullib()
    #     package.docxreplace.replacedocx(self.link, self.docxname, res)
    #     changejson()
    path = os.path.dirname(__file__)

    def __init__(self, docxname, *name_id_num):
        self.docxname = docxname
        self.name_id_num = name_id_num

    def go(self):
        # json中增加违反和依据的法律内容
        old_json = variable.docxreplace()
        save_path = mkdir.save_path()
        law_name = old_json['category']
        if old_json['violation'] == "":
            old_json = loadlaw.law_json(law_name)
        if self.name_id_num:
            old_json['templr'] = old_json['legal_representative']
            old_json['tempid'] = old_json['identification_number']
            old_json['legal_representative'] = self.name_id_num[0]
            old_json['identification_number'] = self.name_id_num[1]
        if self.name_id_num == ():
            old_json['legal_representative'] = old_json['templr']
            old_json['identification_number'] = old_json['tempid']
        new_json = changejson.changejson(old_json)

        docxreplace.replacedocx(save_path, self.docxname, new_json)


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