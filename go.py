from package import allfunc
from flask import Flask, request, render_template, send_file
import io
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '111111'

bootstrap = Bootstrap(app)


class NameForm(FlaskForm):
    company_name = StringField('店名')
    category = SelectField(
        '选择三品一械类别',
        validators=[Required()],
        choices=[('0', '食'), ('1', '药'), ('2', '械'), ('3', '妆')])
    illegal_behavior = SelectField(
        '选择违法行为',
        validators=[Required()],
        choices=[('0', '食'), ('1', '药'), ('2', '械'), ('3', '妆')])
    class_name = StringField('班级：')
    gender = StringField('性别：')
    school_num = StringField('学号：')
    school_time_year = StringField('在校起始时间年')
    school_time_month = StringField('在校起始时间月')
    school_time_year1 = StringField('在校截止时间年')
    school_time_month1 = StringField('在校截止时间月')
    home_address = StringField('家庭通讯地址：')
    personal_tel = StringField('个人联系方式：')
    home_num = StringField('家庭联系方式：')
    reason = StringField('本人申请理由：')
    submit = SubmitField('申请表下载')
    submit1 = SubmitField('清单下载')


# 列出当前目录下所有json文件
allfunc.all_json_name()

jsonname = input('输入json名称：')
# 通过输入的名称读取json文件
old_json = allfunc.load_old_json(jsonname)

# 根据案由新建文件夹
save_path = allfunc.mkdir_save_path(old_json)

links = input('输入序号（1-案源 2-立案 3-调查 4-合议 5-告知 6-决定 7-其他）：')
new_json = allfunc.changejson(old_json)

if links == '1':
    # new_json = allfunc.changejson(old_json)
    allfunc.replacedocx(save_path, '1案件来源登记表', new_json)

elif links == '2':
    happening = allfunc.get_happening(save_path + '/1案件来源登记表.docx')
    # new_json = allfunc.changejson(old_json)
    new_json['happening'] = happening[0]
    allfunc.replacedocx(save_path, '2立案审批表', new_json)

elif links == '3':
    ren = input('1-本人接受调查 2-授权委托人接受调查：')
    tempjson = allfunc.changejson(old_json, ren)
    allfunc.replacedocx(save_path, '7询问调查笔录', tempjson)

    happening = allfunc.get_happening(save_path + '/1案件来源登记表.docx')
    new_json['happening'] = happening[0]

    if ren == '2':
        new_json['legal_representative'], new_json['templr'] = new_json[
            'templr'], new_json['legal_representative']
        new_json['identification_number'], new_json['tempid'] = new_json[
            'tempid'], new_json['identification_number']
        new_json['position'], new_json['temp_position'] = new_json[
            'temp_position'], new_json['position']

    allfunc.replacedocx(save_path, '9案件调查终结报告', new_json)

elif links == '4':
    happening = allfunc.get_happening(save_path + '/1案件来源登记表.docx')
    new_json['happening'] = happening[0]
    allfunc.replacedocx(save_path, '18案件合议记录', new_json)

elif links == '5':
    happening = allfunc.get_happening(save_path + '/1案件来源登记表.docx')
    new_json['happening'] = happening[0]
    allfunc.replacedocx(save_path, '22听证告知书', new_json)
    allfunc.replacedocx(save_path, '26行政处罚事先告知书', new_json)
    allfunc.replacedocx(save_path, '38事先告知送达回执', new_json)

elif links == '6':
    happening = allfunc.get_happening(save_path + '/1案件来源登记表.docx')
    new_json['happening'] = happening[0]
    allfunc.replacedocx(save_path, '27行政处罚决定审批表', new_json)
    allfunc.replacedocx(save_path, '28行政处罚决定书', new_json)
    allfunc.replacedocx(save_path, '38决定书送达回执', new_json)
    allfunc.replacedocx(save_path, '40行政处罚结案报告', new_json)

else:
    other = input('输入文书名称：')
    happening = allfunc.get_happening(save_path + '/1案件来源登记表.docx')
    new_json['happening'] = happening[0]
    allfunc.replacedocx(save_path, other, new_json)
