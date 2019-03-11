"""File containing main ways to interact with the tool."""
from . import container
from . import executable


# FIXME add types
def install(namespace, options):
    """Do whatever needs to be done to create a new executable."""
    container.build_image(options)
    return executable.make(options)
