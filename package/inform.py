# import package.docxmkdir
# import docxreplace
import package.docxreplace
import os

# from Case_template import docxmkdir


class Inform():
    path = os.path.dirname(__file__)
    alljson = package.docxreplace.alljson
    newpath = package.docxreplace.dirname

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