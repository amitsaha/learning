import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', help='Project Name')
@click.option('--location', help='Project Location')
def new():
    click.echo('Create a new project')

@cli.command()
def run():
    click.echo('Run the project')

def main():
    cli()

if __name__ == '__main__':
    main()
