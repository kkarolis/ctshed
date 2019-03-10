"""Utilities to work with generating/building docker images."""

import tempfile
import dataclasses
import subprocess

from . import constants


DOCKERFILE = """
FROM debian:stable
RUN apt install {options.package}
"""


# FIXME slugify name
def get_new_container_image_name(options):
    return f'{constants.PACKAGE_NAME}-{options.package}'


# FIXME add typing
def build(docker_options):
    """Create a Docker image from new scratch file."""
    with tempfile.NamedTemporaryFile() as handle:

        content = DOCKERFILE.format(options=docker_options)
        handle.write(content.encode(constants.FILE_ENCODING))

        image_name = get_new_container_image_name(docker_options)
        subprocess.call(['docker', 'build', '-t', image_name, handle.name])
    return image_name


@dataclasses.dataclass
class DocerImageOptions:
    package: str
