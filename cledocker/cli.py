"""CLI interface to cledocker."""
import click
import sys


from . import cledocker


@click.group()
def main():
    pass


@click.command()
@click.argument('package')
@click.option('--source', default='debian:stable')
def install(package, source):
    # FIXME error handling
    click.secho('running install {}'.format(package), fg='green')
    executable_name = cledocker.install(package, source)
    click.secho(f'executable created at {executable_name}', fg='green')


main.add_command(install)


if __name__ == '__main__':
    sys.exit(main())
