import package.docxmkdir
import package.docxreplace
import package
import os


class Filing():
    path = os.path.dirname(__file__)
    alljson = package.docxreplace.docxreplace()
    newpath = package.docxmkdir.dirname

    def __source(self):
        doc = package.DocxTemplate(Filing.path + "/filing/1案件来源登记表.docx")
        # context = {'num': "122"}
        doc.render(Filing.alljson)
        pathname = package.docxmkdir.pathname
        doc.save(pathname + '/1案件来源登记表.docx')

    def __approval(self):
        doc = package.DocxTemplate(Filing.path + "/filing/2立案审批表.docx")
        # context = {'company_name': Filing.alljson['company_name']}
        doc.render(Filing.alljson)
        pathname = package.docxmkdir.pathname
        doc.save(pathname + '/2立案审批表.docx')

    def go(self):
        self.__source()
        self.__approval()