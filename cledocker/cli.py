"""CLI interface to cledocker."""
import click
import sys


from . import cledocker
from .utils import get_tool_options


@click.group()
def main():
    pass


@click.command()
@click.argument('namespace')
@click.option('--source', default='debian:stable')
@click.option('--cmd')
@click.option('--packages')
def install(namespace, **cli_options):
    # FIXME error handling
    image_options = get_tool_options(cli_options)
    click.secho(f'running install for namespace {namespace}', fg='green')
    executable_name = cledocker.install(namespace, image_options)
    click.secho(f'executable created at {executable_name}', fg='green')


main.add_command(install)


if __name__ == '__main__':
    sys.exit(main())
