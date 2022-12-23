# import logging
# from config.path import logs_path
# import os
#
#
# def loggin_func(name='yns', log_level='ERROR',file=None,file_level='ERROR',
#                 fmt="""%(asctime)s--%(levelname)s--%(filename)s--%(lineno)d--%(message)s"""):
#     logger = logging.getLogger(name)
#     logger.setLevel(log_level)
#     handler = logging.StreamHandler()
#     handler.setLevel(log_level)
#     logger.addHandler(handler)
#     new_fmt = logging.Formatter(fmt)
#     handler.setFormatter(new_fmt)
#     if file:
#         file_handler = logging.FileHandler(file, encoding='utf-8')
#         file_handler.setLevel(file_level)
#         logger.addHandler(file_handler)
#         file_handler.setFormatter(new_fmt)
#     return logger
#
# log = loggin_func(file=os.path.join(logs_path,'yns.log'))
