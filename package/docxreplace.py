# import json
import os
# import pathlib
import docxtpl
# import package.changejson
from package import variable


class Docxreplace():
    # def __init__(self, path, self.alljson, pathname, dirname, fullib_s):
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # self.alljson = docxreplace()
    alljson = variable.old_json

    def replacedocx(self, link, docxname, alljson=alljson):
        doc = docxtpl.DocxTemplate(Docxreplace.path + "/" + "package/" + link +
                                   "/" + docxname + ".docx")
        doc.render(self.alljson)
        doc.save(self.pathname + '/' + docxname + '.docx')
