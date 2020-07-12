import logging

logger = logging.getLogger("logger")
# logger.setLevel(logging.DEBUG) # 全局的。NOTSET（0）、DEBUG（10）、INFO（20）、WARNING（30）、ERROR（40）、CRITICAL（50）
handler1 = logging.StreamHandler() # 输出到控制台
handler1.setLevel(10)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler1.setFormatter(formatter)
logger.addHandler(handler1)

handler2 = logging.FileHandler('./test.log','a', encoding='utf-8')  # 当前目录生成，a:追加
handler2.setLevel(10)
handler1.setFormatter(formatter)
logger.addHandler(handler2)
logger.info('hello')