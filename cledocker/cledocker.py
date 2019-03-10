"""File containing main ways to interact with the tool."""
from . import utils
from . import container


# FIXME add types
def install(package_name):
    options = container.DocerImageOptions(package=package_name)
    image_name = container.build(options)
    executable_name = utils.get_new_executable_name(package_name)
