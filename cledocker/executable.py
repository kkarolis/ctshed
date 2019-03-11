import dataclasses
import os

from . import constants


EXETEMPLATE = """
#!/usr/bin/env sh

docker run \
    --rm \
    --user="$UID" \
    --workdir "$PWD" \
    -a stdin -a stdout -a stderr \
    -i \
    -v "/home:/home" \
    {options.image_name} "$@"
"""


def make(options):
    bin_directory = os.path.expanduser(constants.BIN_DIRECTORY)
    executable_path = os.path.join(bin_directory, options.executable_name)
    with open(executable_path, 'w+b') as handle:
        file_contents = EXETEMPLATE.format(options=options)
        handle.write(file_contents.encode(constants.FILE_ENCODING))
        os.chmod(executable_path, 0o755)
    return executable_path


@dataclasses.dataclass
class ExecutableOptions:
    image_name: str
    executable_name: str
