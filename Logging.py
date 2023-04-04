import logging


def defaultLogging():
    logger = logging.getLogger("")
    format = '%(asctime)s [%(levelname)s] %(message)s'
    formatter = logging.Formatter(format)
    logging.basicConfig(level=logging.DEBUG, format=format, datefmt='%d/%m/%Y %H:%M:%S', filename="debug.log")
    # multiprocessing_logging.install_mp_handler()

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    ch3 = logging.FileHandler("info.log")
    ch3.setLevel(logging.INFO)
    ch3.setFormatter(formatter)

    ch2 = logging.FileHandler("warning.log")
    ch2.setLevel(logging.WARNING)
    ch2.setFormatter(formatter)

    if (logger.hasHandlers()):
        logger.handlers.clear()
    logging.getLogger("").addHandler(ch)
    logging.getLogger("").addHandler(ch2)
    logging.getLogger("").addHandler(ch3)