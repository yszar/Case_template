import package.docxreplace
import pathlib
import os
alljson = package.docxreplace.docxreplace()
# path = os.path.abspath(os.path.dirname(__file__))
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dirname = alljson["company_name"] + alljson["illegal_behavior"] + '案'
pathname = path + '/' + dirname
pathlib.Path(pathname).mkdir(parents=True, exist_ok=True)
