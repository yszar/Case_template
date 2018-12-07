from flask_sqlalchemy import SQLAlchemy


# 实例化
db = SQLAlchemy(app)


class Role(db.Model):
    # 定义表名
    __tablename__ = 'test'
    # 定义列对象
    #    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), primary_key=True)

    # user = db.relationship('User', backref='test')

    # repr()方法显示一个可读字符串，虽然不是完全必要，不过用于调试和测试还是很不错的。
    def __repr__(self):
        return '<test {}> '.format(self.name)


admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')

db.session.add_all([admin_role, mod_role, user_role])

db.session.commit()

print(user_role)
# 数据库测试结束