import logging
from sqlalchemy import Column, String, Boolean
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

    def to_dict(self):
        return {column.name: getattr(self, column.name, None) for column in self.__table__.columns}

    @staticmethod
    def to_json(all_vendors):
        return [vendor.to_dict() for vendor in all_vendors]

    @classmethod
    def get_pwd(cls, conditions: dict):
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
    def get_row_count(cls):
        try:
            with session:
                rows = session.query(cls).count()
                return rows
        except Exception as e:
            logging.error(str(e))


if __name__ == '__main__':
    l1 = PwdMgr().get_pwd({})
    for l in l1:
        print(l.to_dict())

