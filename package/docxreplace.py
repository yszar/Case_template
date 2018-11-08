import json
import os
import pathlib
import docxtpl

path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def docxreplace():
    with open(path + '/information.json', 'r') as f:
        data = json.load(f)
    return data


alljson = docxreplace()
dirname = alljson["company_name"] + alljson["illegal_behavior"] + '案'
pathname = path + '/' + dirname


def replacedocx(link, docxname, alljson=docxreplace()):
    doc = docxtpl.DocxTemplate(path + "/" + "package/" + link + "/" +
                               docxname + ".docx")
    doc.render(alljson)
    doc.save(pathname + '/' + docxname + '.docx')


pathlib.Path(pathname).mkdir(parents=True, exist_ok=True)
