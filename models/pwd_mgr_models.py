import logging

from sqlalchemy import Column, String, Boolean

from models.db_engine import Base, session


class PwdMgr(Base):
    __tablename__ = 'PwdMgr'
    # 字段忽略大小写，方便模糊查询
    pwd_id = Column(String(32), primary_key=True)
    title = Column(String(32, collation='NOCASE'), nullable=False)
    url = Column(String(64, collation='NOCASE'))
    usr = Column(String(32, collation='NOCASE'))
    pwd = Column(String(256, collation='NOCASE'))
    category = Column(String(16, collation='NOCASE'))
    remarks = Column(String(512, collation='NOCASE'))
    create_time = Column(String(32))
    last_update_time = Column(String(32))
    delete_flag = Column(Boolean)
    delete_time = Column(String(32))

    def __init__(self, field_dict: dict):

        self.title = field_dict.get('title')
        self.url = field_dict.get('url')
        self.usr = field_dict.get('usr')
        self.pwd = field_dict.get('pwd')
        self.category = field_dict.get('category')
        self.remarks = field_dict.get('remarks')
        self.create_time = field_dict.get('create_time')
        self.last_update_time = field_dict.get('last_update_time')
        self.delete_flag = field_dict.get('delete_flag')
        self.delete_time = field_dict.get('delete_time')

    def __repr__(self):
        """
        将返回的对象格式化为字符串
        :return:
        """
        return f"<PwdMgr(title='{self.title}', url='{self.url}', " \
               f"usr='{self.usr}',pwd='{self.pwd}', category='{self.category}'," \
               f" remarks='{self.remarks}', create_time='{self.create_time}'," \
               f" last_update_time='{self.last_update_time}')>"

    def to_dict(self):
        return {column.name: getattr(self, column.name, None) for column in self.__table__.columns}

    @staticmethod
    def to_json(all_vendors):
        return [vendor.to_dict() for vendor in all_vendors]

    @classmethod
    def get_pwd(cls, conditions: dict):
        # 多条件查询
        try:
            with session:
                result = session.query(cls).filter(cls.delete_flag == '0')
                if conditions.get('title'):
                    result = result.filter(cls.title.like(f"%{conditions.get('title')}%"))
                if conditions.get('url'):
                    result = result.filter(cls.url.like(f"%{conditions.get('url')}%"))
                if conditions.get('usr'):
                    result = result.filter(cls.usr.like(f"%{conditions.get('usr')}%"))
                if conditions.get('category'):
                    result = result.filter(cls.category == conditions.get('category'))
                if conditions.get('remarks'):
                    result = result.filter(cls.remarks.like(f"%{conditions.get('remarks')}%"))
                print(f"已查询到{len(result.all())}条记录")
                return result.all()
        except Exception as e:
            logging.error(str(e))

    @classmethod
    def insert_pwd(cls, conditions: dict):
        try:
            with session:
                if not conditions.get('title'):
                    logging.error("标题不能为空！")
                else:
                    session.add(cls(field_dict=conditions))
                    session.commit()
        except Exception as e:
            logging.error(str(e))

    @classmethod
    def update_pwd(cls, conditions: dict):
        pass

    @classmethod
    def get_row_count(cls):
        try:
            with session:
                rows = session.query(cls).count()
                return rows
        except Exception as e:
            logging.error(str(e))

    @classmethod
    def get_category(cls):
        category_set = {category.to_dict()['category'] for category in cls.get_pwd({'category': ''}) if
                        len(category.to_dict()['category']) > 0}
        return category_set


if __name__ == '__main__':
    # print([r.to_dict() for r in PwdMgr.get_pwd({})])
    PwdMgr.insert_pwd(
        {'pwd_id': '', 'title': '标题2333', 'url': '地址1', 'usr': '用户1', 'pwd': '密码1', 'category': '分组1', 'remarks': '备注1',
         'create_time': '时间11',
         'last_update_time': '时间12', 'delete_flag': True, 'delete_time': '时间13'})
