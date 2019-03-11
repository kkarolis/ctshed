"""File containing main ways to interact with the tool."""
from . import utils
from . import container
from . import executable


# FIXME add types
def install(namespace, image_options):
    """Do whatever needs to be done to create a new executable."""
    # build the image
    image_name = container.get_new_container_image_name(namespace)
    container.build_image(image_name, image_options)

    # make the executable
    executable_name = utils.get_new_executable_name(namespace)
    executable_options = executable.ExecutableOptions(
        executable_name=executable_name,
        image_name=image_name,
        cmd=image_options.cmd,
    )
    return executable.make(executable_options)
