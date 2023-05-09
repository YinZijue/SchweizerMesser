import logging
from sqlalchemy import Column, String, Boolean, insert
from models.db_engine import Base, session


class PwdMgr(Base):
    __tablename__ = 'PwdMgr'
    # 字段忽略大小写，方便模糊查询
    title = Column(String(32, collation='NOCASE'), primary_key=True)
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
                    result = result.filter(cls.category.like(f"%{conditions.get('category')}%"))
                if conditions.get('remarks'):
                    result = result.filter(cls.remarks.like(f"%{conditions.get('remarks')}%"))
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
                    session.commit()
        except Exception as e:
            logging.error(str(e))

    @classmethod
    def get_row_count(cls):
        try:
            with session:
                rows = session.query(cls).count()
                return rows
        except Exception as e:
            logging.error(str(e))


if __name__ == '__main__':
    # print([r.to_dict() for r in PwdMgr.get_pwd({})])
    PwdMgr.insert_pwd({'title': '标题1', 'url': '地址1', 'usr': '用户1', 'pwd': '密码1', 'category': '分组1', 'remarks': '备注1',
                       'create_time': '时间11',
                       'last_update_time': '时间12', 'delete_flag': True, 'delete_time': '时间13'})
