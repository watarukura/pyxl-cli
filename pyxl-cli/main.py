from typing import List

import click
import sys


def main() -> None:
    sys.exit(cli())


@click.command()
@click.argument("template_xlsx", required=True, type=click.File("rb"))
@click.option(
    "--addresses",
    "-a",
    required=True,
    nargs=2,
    type=click.Tuple([int, str]),
    multiple=True,
    help=("sheet_no and address(like a1)"),
)
@click.argument("input_text_file", required=True, type=click.File("rb"))
@click.argument("output_xlsx", required=True, type=click.File("wb"))
def cli(
    template_xlsx: str,
    addresses: List[str],
    input_text_file: str,
    output_xlsx: str,
) -> None:
    click.echo(f"template: {template_xlsx}")
    for address in addresses:
        click.echo(f"sheet_no: {address[0]}")
        click.echo(f"address: {address[1]}")
    click.echo(f"input_file: {input_text_file}")
    click.echo(f"output_file: {output_xlsx}")


if __name__ == "__main__":
    main()
