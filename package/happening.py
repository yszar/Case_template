from package import mkdir
import docx


def happening():
    save_path = mkdir.save_path()
    doc = docx.Document(save_path + '/1案件来源登记表.docx')
    happening = doc.paragraphs[11]
    return happening
