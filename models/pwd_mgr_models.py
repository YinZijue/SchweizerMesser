import logging

from sqlalchemy import Column, String, Boolean

from config import get_rowtime_stamp, get_moment
from models.db_engine import Base, session


class PwdMgr(Base):
    __tablename__ = 'PwdMgr'
    # 字段忽略大小写，方便模糊查询
    pwd_id = Column(String(16), primary_key=True)
    title = Column(String(32, collation='NOCASE'), nullable=False)
    url = Column(String(64, collation='NOCASE'))
    usr = Column(String(32, collation='NOCASE'))
    password = Column(String(256, collation='NOCASE'))
    category = Column(String(16, collation='NOCASE'))
    remark = Column(String(512, collation='NOCASE'))
    create_time = Column(String(32))
    last_update_time = Column(String(32))
    delete_flag = Column(Boolean)
    delete_time = Column(String(32))

    def __init__(self, field_dict: dict):
        self.pwd_id = get_rowtime_stamp()
        self.title = field_dict.get('title')
        self.url = field_dict.get('url')
        self.usr = field_dict.get('usr')
        self.password = field_dict.get('password')
        self.category = field_dict.get('category')
        self.remark = field_dict.get('remark')
        self.create_time = field_dict.get('create_time')
        self.last_update_time = field_dict.get('last_update_time')
        self.delete_flag = field_dict.get('delete_flag')
        self.delete_time = field_dict.get('delete_time')

    def __repr__(self):
        """
        将返回的对象格式化为字符串
        :return:
        """
        return f"<PwdMgr(pwd_id='{self.pwd_id}',title='{self.title}', url='{self.url}', " \
               f"usr='{self.usr}',pwd='{self.password}', category='{self.category}'," \
               f" remark='{self.remark}', create_time='{self.create_time}'," \
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
                if conditions.get('pwd_id'):
                    result = result.filter(cls.pwd_id == conditions.get('pwd_id'))
                if conditions.get('title'):
                    result = result.filter(cls.title.like(f"%{conditions.get('title')}%"))
                if conditions.get('url'):
                    result = result.filter(cls.url.like(f"%{conditions.get('url')}%"))
                if conditions.get('usr'):
                    result = result.filter(cls.usr.like(f"%{conditions.get('usr')}%"))
                if conditions.get('category'):
                    result = result.filter(cls.category == conditions.get('category'))
                if conditions.get('remark'):
                    result = result.filter(cls.remark.like(f"%{conditions.get('remark')}%"))
                print(f"已查询到{len(result.all())}条记录")
                return result.all()
        except Exception as e:
            logging.error(str(e))

    @classmethod
    def insert_pwd(cls, conditions: dict):
        try:
            with session:
                if not conditions.get('title') or len(conditions.get('title')) == 0:
                    logging.error("标题不能为空！")
                else:
                    try:
                        if conditions.get('title') in session.query(cls.title).filter(
                                cls.title == conditions.get('title')).one():
                            logging.error('标题不允许重复,添加失败,请检查！')
                    except Exception:
                        logging.info("当前标题无历史记录,判定有效.")
                        session.add(cls(field_dict=conditions))
                        session.commit()

        except Exception as e:
            logging.error(str(e))

    @classmethod
    def update_pwd(cls, original_record: dict, new_record: dict):
        try:
            with session:
                exist_title = [title.to_dict()['title'] for title in cls.get_pwd({'title': ''})]
        except Exception as e:
            logging.info(str(e))
        if not new_record.get('title') or len(new_record.get('title')) == 0:
            logging.error('将要保存的标题为空,更新密码记录失败,请检查！')
        elif original_record.get('title') != new_record.get('title') and new_record.get('title') in exist_title:
            logging.error("将要保存的密码已存在,更新失败,请检查!")
        else:
            print("original_record为", original_record)
            try:
                with session:
                    original_pwd = session.query(cls).filter(cls.title == original_record.get('title'))
                    original_pwd.update(new_record)
                    new_pwd = session.query(cls).filter(cls.title == new_record.get('title'))
                    new_pwd.update({'last_update_time': get_moment()})
                    session.commit()
            except Exception as e:
                logging.error(str(e))

    @classmethod
    def delete_pwd_logical(cls, original_record: list):
        title_list = [record['title'] for record in original_record]
        try:
            with session:
                pwd_id_list = [pwd_id for record in session.query(cls.pwd_id).filter(cls.title.in_(title_list)).all()
                               for pwd_id in record]
                session.query(cls).filter(cls.pwd_id.in_(pwd_id_list)).update(
                    {'delete_flag': 1, 'delete_time': get_moment()})
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

    @classmethod
    def get_category(cls):
        with session:
            category_set = {
                category for categories in session.query(cls.category).all() for category in categories if
                len(category) > 0
            }
            # 利用字典键去重
        return category_set


if __name__ == '__main__':
    PwdMgr.delete_pwd_logical([{'title': '网易UU'}, {'title': '腾讯视频'}])
    # print([title for temp in session.query(PwdMgr.title).all() for title in temp])
    # PwdMgr.insert_pwd(conditions={
    #     'title': '腾讯视频',
    #     'url': 'https://www.baidu.com',
    #     'usr': 'JackLondon',
    #     'password': 'sdfasfasfawegaergw3423',
    #     'category': "分组2",
    #     'remark': "这是备注",
    #     'create_time': get_moment(),
    #     'last_update_time': get_moment(),
    #     'delete_flag': 0
    # })
    # PwdMgr.update_pwd(
    #     original_record={
    #         'title': 'tom',
    #         'url': 'sssss',
    #         'usr': '1111',
    #         'password': 'fasfasdfasdf',
    #         'category': "222",
    #         'remark': "111",
    #         'delete_flag': 0
    #     },
    #     new_record=
    #     {
    #         'title': 'tom',
    #         'url': '23234234',
    #         'usr': '1111',
    #         'password': 'fasfasdfasdf',
    #         'category': "222",
    #         'remark': "111",
    #         'delete_flag': 0
    #     }
    # )
