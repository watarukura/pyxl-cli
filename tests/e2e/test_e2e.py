import filecmp
import tempfile

import pytest
from click.testing import CliRunner

from src.main import cli


runner = CliRunner()
temp_dir = tempfile.TemporaryDirectory()
# e2e_test_dir = "tests/e2e/xlsx/"
e2e_test_dir = "tests"


@pytest.mark.parametrize(
    "template_xlsx, sheet_no, address, input_csv, output_xlsx, delimiter, expect",
    (
        (
            f"{e2e_test_dir}template.xlsx",
            "1",
            "a1",
            f"{e2e_test_dir}input.csv",
            f"{temp_dir}output.xlsx",
            ",",
            f"{e2e_test_dir}output.xlsx",
        )
    ),
)
def test_cli(
    template_xlsx: str,
    sheet_no: str,
    address: str,
    input_csv: str,
    output_xlsx: str,
    delimiter: str,
    expect: str,
):
    runner.invoke(
        cli,
        args=[
            template_xlsx,
            "-T",
            sheet_no,
            address,
            input_csv,
            output_xlsx,
            "--delimiter",
            delimiter,
        ],
    )
    assert filecmp.cmp(output_xlsx, expect)
