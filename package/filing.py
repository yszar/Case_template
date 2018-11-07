import package.docxmkdir
import package.docxreplace
import package
import os
# from Case_template import docxmkdir


class Filing():
    path = os.path.dirname(__file__)
    alljson = package.docxreplace.docxreplace()
    newpath = package.docxmkdir.dirname
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

    # def go(self):
    #     self.__init__()
        # self.__approval()