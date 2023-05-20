def page_switched(main_window):
    """
    主菜单切换
    :param main_window:
    :return:
    """
    treeWidget = main_window.treeWidget
    item = treeWidget.currentItem()
    for index in range(main_window.stack_list.count()):
        if item.text(0) == main_window.stack_list.widget(index).accessibleName():
            main_window.stack_list.setCurrentIndex(index)
