"""Utilities to work with generating/building docker images."""

import dataclasses
import subprocess
import os

from . import constants
from . import utils


DOCKERFILE = """
FROM {options.source_image}
"""

# FIXME in some images this will not work, optional ?
# RUN apt-get update && apt-get -y -q install \
#         {options.package} \
#     && rm -rf /var/lib/apt/lists/*

# FIXME slugify name
def get_new_container_image_name(options):
    return f'{constants.PACKAGE_NAME}-{options.package}'


# FIXME add typing
def build(docker_options):
    """Create a Docker image from new scratch file."""
    with utils.NamedTemporaryDir() as tmp_dir:
        with open(os.path.join(tmp_dir, 'Dockerfile'), 'w+b') as handle:
            content = DOCKERFILE.format(options=docker_options)
            handle.write(content.encode(constants.FILE_ENCODING))

        image_name = get_new_container_image_name(docker_options)
        subprocess.call(['docker', 'build', '-t', image_name, tmp_dir])

    # FIXME ability to retry ?
    return image_name


@dataclasses.dataclass
class DockerImageOptions:
    package: str
    source_image: str = 'debian:stable'
