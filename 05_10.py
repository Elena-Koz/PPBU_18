# def decor(func):
#     def wrapper():
#         print('BEFORE')
#         func()
#         print('AFTER')
#     return wrapper
# @decor proba():
# def proba():
#     print('PROBA')

# decor(proba)()
#
# def time_run(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         duration = round(end - start, 2)
#      return wrapper
#
# def decor(func):
#     def wrapper():
#         print('BEFORE')
#         func()
#         print('AFTER')
# def etalon (n):
#     print('ETALON')
#     time.sleep(n)
#
#
#
#
# etalon (3)
#
#
#     return wrapper