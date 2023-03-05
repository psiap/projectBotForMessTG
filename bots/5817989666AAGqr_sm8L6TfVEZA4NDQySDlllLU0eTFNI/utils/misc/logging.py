import logging

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    #filename="py_log.log",
                    #filemode="a"
                    # level=logging.DEBUG,  # Можно заменить на другой уровень логгирования.
                    )
