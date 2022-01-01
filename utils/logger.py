import logging


def logger_setup(config: dict):
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s| %(message)s', '%m-%d|%H:%M:%S')

    if not config.get('no_console_output', False):
        console_hdl = logging.StreamHandler()
        console_hdl.setFormatter(formatter)
        root_logger.addHandler(console_hdl)
