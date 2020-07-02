import csv
import sys
from typing import Any, List

import click

from src.excel import write_xlsx


def main() -> None:
    sys.exit(cli())


@click.command()
@click.argument("template_xlsx", required=True, type=click.Path(exists=True))
@click.option(
    "--sheet_xy_csv",
    "-T",
    required=True,
    nargs=3,
    type=click.Tuple([int, str, click.Path(exists=True)]),
    multiple=True,
    help=("sheet_no and address(like a1) and input csv"),
)
@click.argument("output_xlsx", required=True, type=click.File("wb"))
@click.option("--delimiter", default=",", type=str, help="csv delimiter")
def cli(
    template_xlsx: str,
    sheet_xy_csv: List[Any],
    output_xlsx: str,
    delimiter: str,
) -> None:
    for sheet_no, address, input_file in sheet_xy_csv:
        with open(input_file) as f:
            reader = csv.reader(f)
            input_csv = [row for row in reader]
        write_xlsx(template_xlsx, sheet_no, address, input_csv, output_xlsx)


if __name__ == "__main__":
    main()
