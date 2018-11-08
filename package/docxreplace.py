# import json
import os
import pathlib
import docxtpl
import package.changejson

path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# alljson = docxreplace()
alljson = package.changejson.changejson()
pathname = ''
dirname = ''


def fullib(food_name, harmful):
    if alljson['illegal_behavior'] == '超过食品安全标准限量的':
        alljson['fullib'] = harmful + '超过食品安全标准限量的' + food_name

    global dirname
    dirname = alljson["company_name"] + alljson["fullib"] + '案'
    global pathname
    pathname = path + '/' + dirname

    pathlib.Path(pathname).mkdir(parents=True, exist_ok=True)


aj = package.changejson.docxreplace()


def replacedocx(link, docxname, alljson=alljson):
    doc = docxtpl.DocxTemplate(path + "/" + "package/" + link + "/" +
                               docxname + ".docx")
    doc.render(alljson)
    doc.save(pathname + '/' + docxname + '.docx')

