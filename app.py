import click
from driver import Driver


@click.command()
@click.option('--file', help="Input File Path")
def run(file):
    driver = Driver(file)
    driver.drive()


if __name__ == "__main__":
    run()
