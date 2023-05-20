import datetime
import time


def get_moment():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


def get_rowtime_stamp():
    return str(time.time()).replace('.', '')[:16]
