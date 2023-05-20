# 查询用户并更新表格数据
from demo.table.user_model import User, Session


def query_users(my_window):
    # 获取查询条件
    query = my_window.query_edit.text()

    # 创建数据库会话
    session = Session()

    # 使用 SQLAlchemy 查询数据库
    users = session.query(User).filter(User.name.like(f'%{query}%')).all()
    print(users)
    # 获取表格模型
    model = my_window.tableView.model()

    # 如果查询结果小于固定行数，使用空行填充表格
    while len(users) < model.rowCount():
        users.append(User())

    # 更新表格数据
    model.beginResetModel()
    model._data = users
    model.endResetModel()

    # 关闭数据库会话
    session.close()
