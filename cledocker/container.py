"""Utilities to work with generating/building docker images."""

import os

import jinja2

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


# FIXME add typing
# FIXME add logging
def build_image(options):
    """Create a Docker image from new scratch file."""
    image_name = options.image_name
    with utils.NamedTemporaryDir() as tmp_dir:
        with open(os.path.join(tmp_dir, 'Dockerfile'), 'w+b') as handle:
            content = DOCKERFILE.render(options=options)
            handle.write(content.encode(constants.FILE_ENCODING))

        # FIXME use distutils to check for the executable
        utils.run_docker_build(image_name, tmp_dir)

    # FIXME ability to retry ?
    return image_name
