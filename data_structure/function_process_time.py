"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/6/3
  Time: 15:29
 """
__author__ = 'liujianhan'
import time
from functools import wraps


class RuntimeTest:
    def __init__(self):
        pass

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kw):
            start_time = time.perf_counter_ns()
            print(func(*args, **kw))
            end_time = time.perf_counter_ns()
            cost = (end_time - start_time) / 1000000
            print(f"{func.__name__} 函数的运行时间为 {cost} ms.")
            print('=============================')
        return wrapper


def print_time(func):
    @wraps(func)
    def wrapper(*args, **kw):
        start_time = time.perf_counter_ns()
        print(func(*args, **kw))
        end_time = time.perf_counter_ns()
        cost = (end_time - start_time) / 1000000
        print(f"{func.__name__} 函数的运行时间为 {cost} ms.")
        print('============')
    return wrapper
