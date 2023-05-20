import logging
import os.path

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base, sessionmaker

# 使用相对路径连接数据库，似乎是针对当前文件所在目录
root = os.path.dirname(os.getcwd())
engine = create_engine(f'sqlite:///{root}/db/db.db3', echo=True, connect_args={'check_same_thread': False})
Session = sessionmaker(engine, autocommit=False, autoflush=False)
session = Session()
Base = declarative_base()
insp = inspect(engine)

column_map = {'pwd_id': '密码ID', 'title': "标题", 'url': "服务地址", 'usr': "用户名", 'password': "密码", 'category': "分组",
              'remark': "备注",
              'create_time': "创建时间", 'last_update_time': "更新时间", 'delete_flag': "删除标识", 'delete_time': "删除时间"}


# 表名映射
def column_mapping(col_name: str, col_dict: dict):
    for k, v in col_dict.items():
        if col_name == k:
            return v
        elif col_name == v:
            return k


def get_column_info(table_name):
    # 分别获取当前数据库、表名以及表中所有列的信息
    current_db = insp.get_schema_names()[0]
    columns = insp.get_columns(table_name=table_name, schema=current_db)
    return [column_mapping(column["name"], column_map) for column in columns]


def insert_db(db_model):
    try:
        with session:
            session.add(db_model)
            session.commit()
            session.refresh(db_model)
            logging.info("增加记录成功")
    except Exception as e:
        logging.error(f"增加记录异常,{e}")
        session.rollback()
        session.flush()


if __name__ == '__main__':
    print(get_column_info('PwdMgr'))

