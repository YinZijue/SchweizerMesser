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

column_map = {'title': "标题", 'url': "服务地址", 'usr': "用户名", 'pwd': "密码", 'category': "分组", 'remarks': "备注",
              'create_time': "创建时间", 'last_update_time': "更新时间", 'delete_flag': "删除标识", 'delete_time': "删除时间"}


# 表名映射
def column_mapping(col_list: list, col_dict: dict):
    return [v for k, v in col_dict.items() if k in col_list]


def get_column_info():
    # 分别获取当前数据库、表名以及表中所有列的信息
    current_db = insp.get_schema_names()[0]
    current_table = insp.get_table_names(schema=current_db)[0]
    columns = insp.get_columns(table_name=current_table, schema=current_db)
    # 提取出列名,并映射为中文
    column_list = column_mapping([column['name'] for column in columns], column_map)
    main_col = column_list[1:8]
    return {'main_col': main_col, 'main_col_count': len(main_col), 'del_col': column_list,
            'del_col_count': len(column_list)}


if __name__ == '__main__':
    print(get_column_info())
