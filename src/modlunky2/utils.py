import contextlib
import logging
import sys
import traceback
import os
from functools import wraps

from modlunky2.assets.patcher import Patcher

logger = logging.getLogger("modlunky2")


def is_patched(exe_filename):
    with exe_filename.open("rb") as exe:
        return Patcher(exe).is_checksum_patched()


def log_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:  # pylint: disable=broad-except
            logger.exception("Unexpected failure")

    return wrapper


def tb_info():
    return "".join(traceback.format_exception(*sys.exc_info())).strip()


@contextlib.contextmanager
def temp_chdir(new_dir):
    old_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(old_dir)
