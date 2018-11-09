# import os
import docxtpl
from package import variable

# class Docxreplace():
#     path = variable.path

#     def __init__(self, new_json):
#         # path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

#         # self.alljson = docxreplace()
#         self.new_json = new_json


def replacedocx(save_path, docxname, new_json):
    doc = docxtpl.DocxTemplate(variable.path + "/" + "package/" + 'docxs' +
                               "/" + docxname + ".docx")
    doc.render(new_json)
    doc.save(save_path + "/" + docxname + '.docx')
