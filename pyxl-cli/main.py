import click
from typing import List


def main() -> None:
    cli()


@click.command()
@click.argument("template", required=True, type=click.File("rb"))
@click.argument("sheet_no", required=True, nargs=-1, type=int)
@click.argument("address", required=True, nargs=-1, type=str)
@click.argument("input_file", required=True, type=click.File("rb"))
@click.argument("output_file", required=True, type=click.File("wb"))
def cli(
    template: str, sheet_no: List[int], address: List[str], input_file: str, output_file: str
) -> None:
    pass


if __name__ == "__main__":
    main()
