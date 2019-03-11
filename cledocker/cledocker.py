"""File containing main ways to interact with the tool."""
from . import utils
from . import container
from . import executable


# FIXME add types
def install(package_name, source):
    """Do whatever needs to be done to create a new executable."""
    # build the image
    docker_options = container.DockerImageOptions(
        package=package_name,
        source_image=source,
    )
    image_name = container.build(docker_options)

    # make the executable
    executable_name = utils.get_new_executable_name(package_name)
    executable_options = executable.ExecutableOptions(
        executable_name=executable_name,
        image_name=image_name,
    )
    return executable.make(executable_options)
