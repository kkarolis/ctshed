"""Utilities to work with generating/building docker images."""

import dataclasses
import subprocess
import os

import jinja2

from typing import List

from . import constants
from . import utils


DOCKERFILE = jinja2.Template("""
FROM {{options.source_image}}

{% if options.packages -%}
RUN apt-get update && apt-get -y -q install \\
{% for package in options.packages -%}
        {{package}} \\
{% endfor -%}
    && rm -rf /var/lib/apt/lists/*
{% endif -%}
{% if options.cmd -%}
CMD ["{{options.cmd}}"]
{% endif -%}
""")


# FIXME slugify name
def get_new_container_image_name(namespace):
    return f'{constants.PACKAGE_NAME}-{namespace}'


# FIXME add typing
def build_image(image_name, docker_options):
    """Create a Docker image from new scratch file."""
    with utils.NamedTemporaryDir() as tmp_dir:
        with open(os.path.join(tmp_dir, 'Dockerfile'), 'w+b') as handle:
            content = DOCKERFILE.render(options=docker_options)
            handle.write(content.encode(constants.FILE_ENCODING))

        subprocess.call(['docker', 'build', '-t', image_name, tmp_dir])

    # FIXME ability to retry ?
    return image_name


@dataclasses.dataclass
class DockerImageOptions:
    cmd: str
    source_image: str = 'debian:stable'
    packages: List[str] = dataclasses.field(default_factory=list)
