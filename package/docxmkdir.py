import package.docxreplace
import pathlib
alljson = package.docxreplace.docxreplace()

dirname = alljson["company_name"] + alljson["illegal_behavior"] + '案'
pathname = '/home/yszar/文档/广武门案件/Case_template/' + dirname

pathlib.Path(pathname).mkdir(
    parents=True, exist_ok=True)
