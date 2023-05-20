from sqlalchemy import Column, String

from config import get_rowtime_stamp
from models.db_engine import Base


class DataDict(Base):
    __tablename__ = 'DataDict'
    dt_dict_category_id = Column(String(16), primary_key=True)
    dt_dict_category_name = Column(String(16), nullable=False)
    dt_dict_category_value = Column(String(16, collation='NOCASE'), nullable=False)

    def __init__(self, field_dict: dict):
        self.dt_dict_category_id = get_rowtime_stamp()
        self.dt_dict_category_name = field_dict.get('dt_dict_category_name')
        self.dt_dict_category_value = field_dict.get('dt_dict_category_value')

    def __repr__(self):
        """
        将返回的对象格式化为字符串
        :return:
        """
        return f"<PwdMgr(dt_dict_category_id='{self.dt_dict_category_id}'," \
               f"dt_dict_category_name='{self.dt_dict_category_name}', " \
               f"dt_dict_category_value='{self.dt_dict_category_value}')>"

    def to_dict(self):
        return {column.name: getattr(self, column.name, None) for column in self.__table__.columns}