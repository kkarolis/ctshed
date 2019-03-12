"""General purpose utilities not belonging anywhere."""

import contextlib
import tempfile
import shutil
import subprocess

from . import options
from . import constants


def _get_new_executable_name(namespace):
    return f'{constants.PACKAGE_NAME}-{namespace}'


# FIXME slugify name
def _get_new_image_name(namespace):
    return f'{constants.PACKAGE_NAME}-{namespace}'


def run_docker_build(image_name, build_context_dir):
    subprocess.call([  # pragma: nocover
        'docker', 'build', '-t', image_name, build_context_dir]
    )


def _default(value, default):
    """Return default value if value is None."""
    if value is None:
        return default
    return value


def get_tool_options(namespace, cli_options):
    packages = cli_options.get('packages')
    return options.Options(
        source_image=_default(
            cli_options.get('source'), constants.DEFAULT_IMAGE
        ),
        packages=packages.split(',') if packages else [],
        executable_name=_get_new_executable_name(namespace),
        image_name=_get_new_image_name(namespace),
        path=_default(cli_options.get('path'), constants.BIN_DIRECTORY),
        cmd=cli_options.get('cmd'),
    )


@contextlib.contextmanager
def NamedTemporaryDir():
    tmp_dir = tempfile.mkdtemp()
    try:
        yield tmp_dir
    finally:
        shutil.rmtree(tmp_dir)
