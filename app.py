from flask import Flask, request, render_template, redirect
# from flask import Flask, request, render_template, send_file
# from docx import Document
# import io
# from docx.shared import Inches, Pt
# from docx.oxml.ns import qn
# from docx.enum.text import WD_ALIGN_PARAGRAPH
# import time
# import datetime
# from package.NameForm import NameForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
# from urllib.parse import quote
# from package.caseDB import store_manager, app, db
# from package.index_nav import nav
from flask_nav import Nav
from flask_nav.elements import View, Navbar
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '111111'

# 数据库测试开始
# 这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名jianshu,连接方式参考 \
# http://docs.sqlalchemy.org/en/latest/dialects/mysql.html
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+pymysql://root:Andylau1987212!@39.107.81.83:3306/caseDB')
# 设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 实例化
db = SQLAlchemy(app)


class store_manager(db.Model):
    # 定义表名
    __tablename__ = 'case_information'
    # 定义列对象
    #    id = db.Column(db.String(64), primary_key=True)
    # id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(64), primary_key=True)
    illegal_behavior = db.Column(db.String(64), primary_key=True)
    address = db.Column(db.String(64))
    category = db.Column(db.String(64))
    business_license = db.Column(db.String(64))
    legal_representative = db.Column(db.String(64))
    identification_number = db.Column(db.String(64))
    gender = db.Column(db.String(64))
    age = db.Column(db.String(64))
    position = db.Column(db.String(64))
    telephone_number = db.Column(db.String(64))
    violation = db.Column(db.String(64))
    violation_content = db.Column(db.String(64))
    food = db.Column(db.String(64))
    har = db.Column(db.String(64))
    according = db.Column(db.String(64))
    according_content = db.Column(db.String(64))
    num = db.Column(db.String(64))

    # user = db.relationship('User', backref='test')

    # repr()方法显示一个可读字符串，虽然不是完全必要，不过用于调试和测试还是很不错的。
    def __repr__(self):
        return '<store_manager {}> '.format(self.name)


# 数据库测试结束
bootstrap = Bootstrap(app)
nav = Nav()
nav.register_element(
    'top',
    Navbar(
        u'行政处罚案件制作系统',
        View(u'首页', 'index'),
        View(u'案件来源登记表', 'case_source'),
        View(u'立案阶段', 'index'),
        View(u'调查阶段', 'index'),
        View(u'合议阶段', 'index'),
        View(u'告知阶段', 'index'),
        View(u'执行阶段', 'index'),
        View(u'其他文书', 'index'),
    ),
)

nav.init_app(app)


class NameForm(FlaskForm):
    company_name = StringField('店名')
    category = SelectField(
        '选择三品一械类别：',
        validators=[Required()],
        choices=[('0', '请选择'), ('1', '食'), ('2', '药'), ('3', '械'), ('4', '妆')])
    illegal_behavior = SelectField(
        '选择违法行为：', validators=[Required()], choices=[
            ('0', '请选择'),
        ])
    food = StringField('食品名称')
    har = StringField('超标的物质')
    address = StringField('地址：')
    legal_representative = StringField('法人（负责人）姓名：')
    telephone_number = StringField('负责人电话号码：')
    identification_number = StringField('法人（负责人）身份证号')
    business_license = StringField('营业执照号')
    num = StringField('立案号')
    position = StringField('职务')
    illegal_label = StringField('违法标签')
    submit = SubmitField('提交信息')
    submit1 = SubmitField('清单下载')


@app.route('/case_source', methods=['GET', 'POST'])
def case_source():
    return render_template('case_source.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    company_name = None
    form = NameForm()
    if form.validate_on_submit():
        # if request.form['stname'] == 'submit':
        # name = NameForm.data['name']
        #        json_name = (str(form.name.data) + \
        # str(form.illegal_behavior.data))

        company_name = form.company_name.data
        illegal_behavior = form.illegal_behavior.data
        address = form.address.data
        category = form.category.choices[int(form.category.data)][1]
        business_license = form.business_license.data
        legal_representative = form.legal_representative.data
        identification_number = form.identification_number.data
        # gender = form.gender.data
        # age = form.age.data
        position = form.position.data
        telephone_number = form.telephone_number.data
        # violation = form.violation.data
        # violation_content = form.violation_content.data
        food = form.food.data
        har = form.har.data
        # according = form.according.data
        # according_content = form.according_content.data
        num = form.num.data
        # form.name.data = ''

        # nt = datetime.datetime.now()
        # admin_role = Role(name='Admin')
        # mod_role = Role(name='Moderator')
        # user_role = Role(name='User')
        # legal_representative_SM = store_manager(
        #     legal_representative=legal_representative)
        # telephone_number_SM = (store_manager \
        # (telephone_number=telephone_number))
        # position_SM = store_manager(position=position)
        # identification_number_SM = store_manager(
        #     identification_number=identification_number)
        store_manager_table = store_manager(
            company_name=company_name,
            illegal_behavior=illegal_behavior,
            address=address,
            category=category,
            business_license=business_license,
            legal_representative=legal_representative,
            identification_number=identification_number,
            # gender=gender,
            # age=age,
            position=position,
            telephone_number=telephone_number,
            # violation=violation,
            # violation_content=violation_content,
            food=food,
            har=har,
            # according=according,
            # according_content=according_content,
            num=num)
        db.session.add_all([store_manager_table])
        db.session.commit()

        # 测试读取数据库
        # result = store_manager.query.filter(
        #    store_manager.legal_representative == '张三').all()

        # if request.form['key'] == '提交信息':
        #     document = Document()
        #     document.styles['Normal'].font.name = u'宋体'
        #     document.styles['Normal']._element.rPr.rFonts.set(
        #         qn('w:eastAsia'), u'宋体')
        #     p = document.add_paragraph()
        #     p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     r = p.add_run('X X X X X X 学 院\rXXX申请表')
        #     r.font.size = Pt(16)
        #     r.bold = True

        #     table = document.add_table(rows=37, cols=13, style='Table Grid')
        #     table.autofit = False
        #     table.columns[0].width = Inches(0.49)
        #     table.cell(0, 0).merge(table.cell(2, 2))
        #     table.cell(0, 3).merge(table.cell(2, 6))
        #     table.cell(0, 7).merge(table.cell(2, 9))
        #     table.cell(0, 10).merge(table.cell(2, 12))
        #     table.cell(3, 0).merge(table.cell(5, 2))
        #     table.cell(3, 3).merge(table.cell(5, 5))
        #     table.cell(3, 6).merge(table.cell(5, 6))
        #     table.cell(3, 7).merge(table.cell(5, 9))
        #     table.cell(3, 10).merge(table.cell(5, 10))
        #     table.cell(3, 11).merge(table.cell(5, 12))
        #     table.cell(6, 0).merge(table.cell(8, 2))
        #     table.cell(6, 3).merge(table.cell(8, 12))
        #     table.cell(9, 0).merge(table.cell(14, 2))
        #     table.cell(9, 3).merge(table.cell(14, 6))
        #     table.cell(9, 7).merge(table.cell(11, 9))
        #     table.cell(12, 7).merge(table.cell(14, 9))
        #     table.cell(9, 10).merge(table.cell(11, 12))
        #     table.cell(12, 10).merge(table.cell(14, 12))
        #     table.cell(15, 0).merge(table.cell(20, 2))
        #     table.cell(15, 3).merge(table.cell(20, 12))
        #     table.cell(21, 0).merge(table.cell(26, 2))
        #     table.cell(21, 3).merge(table.cell(26, 12))
        #     table.cell(27, 0).merge(table.cell(31, 2))
        #     table.cell(27, 3).merge(table.cell(31, 12))
        #     table.cell(32, 0).merge(table.cell(36, 2))
        #     table.cell(32, 3).merge(table.cell(36, 12))
        #     hdr_cells0 = table.rows[0].cells
        #     hdr_cells3 = table.rows[3].cells
        #     hdr_cells6 = table.rows[6].cells
        #     hdr_cells9 = table.rows[9].cells
        #     hdr_cells12 = table.rows[12].cells
        #     hdr_cells15 = table.rows[15].cells
        #     hdr_cells21 = table.rows[21].cells
        #     hdr_cells27 = table.rows[27].cells
        #     hdr_cells32 = table.rows[32].cells

        #     hdr_cells0[0].add_paragraph(
        #         '院（系）\n').alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells0[3].add_paragraph(
        #         departments + '院').alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells0[7].add_paragraph(
        #         '专业班级').alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells0[10].add_paragraph(
        #         specialty + class_name).alignment = WD_ALIGN_PARAGRAPH.CENTER

        #     hdr_cells3[0].add_paragraph(
        #         '姓名\n').alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells3[3].add_paragraph(
        #         name).alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells3[6].add_paragraph(
        #         '性别').alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells3[7].add_paragraph(
        #         gender).alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells3[10].add_paragraph(
        #         '学号').alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells3[11].add_paragraph(
        #         school_num).alignment = WD_ALIGN_PARAGRAPH.CENTER

        #     hdr_cells6[0].add_paragraph(
        #         '在校时间\n').alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells6[3].add_paragraph(
        #         school_time_year + '年' + school_time_month + '月——' +
        #         school_time_year1 + '年' + school_time_month1 +
        #         '月').alignment = WD_ALIGN_PARAGRAPH.CENTER

        #     hdr_cells9[0].add_paragraph(
        #         '家庭通讯地址').alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells9[3].add_paragraph(
        #         home_address).alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells9[7].add_paragraph(
        #         '家庭联系方式').alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells12[7].add_paragraph(
        #         '个人联系方式').alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells9[10].add_paragraph(
        #         home_num).alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells12[10].add_paragraph(
        #         personal_tel).alignment = WD_ALIGN_PARAGRAPH.CENTER

        #     hdr_cells15[0].add_paragraph(
        #         '\n\n本人申请理由').alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells15[3].add_paragraph(
        #         reason + '\n\n学生本人签名：' +
        #         '\n\n\t\t年\t月\t日').alignment = WD_ALIGN_PARAGRAPH.CENTER

        #     hdr_cells21[0].add_paragraph(
        #         '\n\n院系领导意见').alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells21[3].add_paragraph(
        #         '\n\n领导签字：' +
        #         '\n\n\t\t年\t月\t日').alignment = WD_ALIGN_PARAGRAPH.CENTER

        #     hdr_cells27[0].add_paragraph(
        #         '\n\n学生处意见').alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells27[3].add_paragraph(
        #         '\n\n领导签字：' +
        #         '\n\n\t\t年\t月\t日').alignment = WD_ALIGN_PARAGRAPH.CENTER

        #     hdr_cells32[0].add_paragraph(
        #         '\n\n主管校领导审批').alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     hdr_cells32[3].add_paragraph(
        #         '\n\n领导签字：' +
        #         '\n\n\t\t年\t月\t日').alignment = WD_ALIGN_PARAGRAPH.CENTER

        #     # document.save(name + 'XX申请表.docx')
        #     f = io.BytesIO()
        #     document.save(f)
        #     # length = f.tell()
        #     f.seek(0)
        #     filename = quote(name + '申请表.doc')
        #     rv = send_file(f, \
        #     as_attachment=True, attachment_filename=filename)
        #     rv.headers[
        #         'Content-Disposition'] += "; filename*=utf-8''{}".format(
        #             filename)
        #     return rv
        # elif request.form['key'] == '清单下载':
        #     document1 = Document()
        #     document1.styles['Normal'].font.name = u'宋体'
        #     document1.styles['Normal']._element.rPr.rFonts.set(
        #         qn('w:eastAsia'), u'宋体')
        #     p1 = document1.add_paragraph()
        #     p1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     p1.paragraph_format.line_spacing = Pt(25)
        #     r1 = p1.add_run('X X X X X X X X\rX X 清 单\n')
        #     r1.font.size = Pt(16)
        #     r1.bold = True

        #     leave_name = document1.add_paragraph('各部门：\n\n\t')
        #     leave_name.add_run(departments).font.underline = True
        #     leave_name.add_run('院（系）')
        #     leave_name.add_run(specialty).font.underline = True
        #     leave_name.add_run('专业')
        #     leave_name.add_run(class_name).font.underline = True
        #     leave_name.add_run('班,学生')
        #     leave_name.add_run(name).font.underline = True
        #     leave_name.add_run('，（学号：')
        #     leave_name.add_run(school_num).font.underline = True
        #     leave_name.add_run('）。申请')
        #     leave_name.add_run('XX').font.underline = True
        #     leave_name.add_run(',请予以协助办理相关XX手续。')
        #     leave_name.add_run(
        #         '\n\n\n\n\t\t\t\t\t\t\t\t\tX X 处  （公 章）
        # \n\n\t\t\t\t\t\t\t\t\t')
        #     leave_name.add_run(
        #         nt.strftime('%Y{y}%m{m}%d{d}\n\n\n\n\n\n\n').format(
        #             y='年', m='月', d='日'))

        #     table1 = document1.add_table(rows=10, cols=8, style='Table Grid')
        #     table1.cell(0, 0).merge(table1.cell(7, 3))
        #     table1.cell(0, 4).merge(table1.cell(7, 7))
        #     table1.cell(8, 0).merge(table1.cell(9, 7))

        #     hdr1_cells0 = table1.rows[0].cells
        #     hdr1_cells1 = table1.rows[8].cells

        #     dormitory = hdr1_cells0[0].add_paragraph()
        #     dormitory.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     dormitory1 = dormitory.add_run('XXX\n\n\n（盖章）\n\n\t\t年  月  日')
        #     dormitory1.bold = True
        #     dormitory1.font.size = Pt(14)

        #     library = hdr1_cells0[4].add_paragraph()
        #     library.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        #     library1 = library.add_run('XXX\n\n\n（盖章）\n\n\t\t年  月  日')
        #     library1.bold = True
        #     library1.font.size = Pt(14)

        #     note = hdr1_cells1[0].add_paragraph()
        #     note1 = note.add_run('备注：\n')
        #     note1.bold = True
        #     note1.font.size = Pt(12)

        #     f = io.BytesIO()
        #     document1.save(f)
        #     # length = f.tell()
        #     f.seek(0)
        #     filename = quote(name + '清单.doc')
        #     rv = send_file(f, as_attachment=True,
        # attachment_filename=filename)
        #     rv.headers[
        #         'Content-Disposition'] += "; filename*=utf-8''{}".format(
        #             filename)
        #     return rv
        return redirect('/case_source')
    return render_template('index.html', form=form, company_name=company_name)


if __name__ == '__main__':
    app.run()
