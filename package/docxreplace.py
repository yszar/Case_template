# import json
import os
import pathlib
import docxtpl
# import package.changejson
from package import variable


class Docxreplace():
    # def __init__(self, path, self.alljson, pathname, dirname, fullib_s):
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # self.alljson = docxreplace()
    alljson = variable.old_json

    # global pathname
    pathname = ''
    # global dirname
    dirname = ''

    fullib_s = ''

    def fullib(self, food_name, harmful):
        if self.alljson['illegal_behavior'] == '超过食品安全标准限量的':
            self.alljson['fullib'] = harmful + '超过食品安全标准限量的' + food_name
        global fullib_s
        fullib_s = self.alljson['fullib']
        global dirname
        dirname = self.alljson["company_name"] + self.alljson["fullib"] + '案'
        global pathname
        pathname = self.path + '/' + dirname

        pathlib.Path(pathname).mkdir(parents=True, exist_ok=True)
        # return pathname, dirname

    def replacedocx(self, link, docxname, alljson=alljson):
        doc = docxtpl.DocxTemplate(self.path + "/" + "package/" + link + "/" +
                                   docxname + ".docx")
        doc.render(self.alljson)
        doc.save(pathname + '/' + docxname + '.docx')
