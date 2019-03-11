import dataclasses
import os
import jinja2

from . import constants


EXETEMPLATE = jinja2.Template("""
#!/usr/bin/env sh

docker run \\
    --rm \\
    --user="$UID" \\
    --workdir "$PWD" \\
    -a stdin -a stdout -a stderr \\
    -i \\
    -v "/home:/home" \\
    {{options.image_name}} \\
{% if options.cmd -%}
    {{options.cmd}} \\
{% endif -%}
    "$@"
""")


def make(options):
    bin_directory = os.path.expanduser(options.path)
    executable_path = os.path.join(bin_directory, options.executable_name)
    with open(executable_path, 'w+b') as handle:
        file_contents = EXETEMPLATE.render(options=options)
        handle.write(file_contents.encode(constants.FILE_ENCODING))
        os.chmod(executable_path, 0o755)
    return executable_path
