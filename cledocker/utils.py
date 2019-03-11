"""General purpose utilities not belonging anywhere."""

import contextlib
import tempfile
import shutil


def get_new_executable_name(install_name):
    return f'cledocker-{install_name}'


@contextlib.contextmanager
def NamedTemporaryDir():
    tmp_dir = tempfile.mkdtemp()
    try:
        yield tmp_dir
    finally:
        shutil.rmtree(tmp_dir)
