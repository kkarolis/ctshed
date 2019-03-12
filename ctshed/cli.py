"""CLI interface to ctshed."""
import click
import sys


from . import ctshed
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
    options = get_tool_options(namespace, cli_options)
    click.secho(f'running install for namespace {namespace}', fg='green')
    executable_name = ctshed.install(namespace, options)
    click.secho(f'executable created at {executable_name}', fg='green')


main.add_command(install)


if __name__ == '__main__':
    sys.exit(main())
