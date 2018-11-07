import os
import package
import json
import docxtpl
# import package.docxmkdir
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def docxreplace():
    with open(path + '/information.json', 'r') as f:
        data = json.load(f)
    return data


def replacedocx(self, path, link, docxname):
    doc = package.DocxTemplate(path + "/" + self.link + "/" + self.docxname +
                               ".docx")
    # context = {'num': "122"}
    doc.render(package.filing.Filing.alljson)
    pathname = package.docxmkdir.pathname
    doc.save(pathname + '/' + self.docxname + '.docx')
