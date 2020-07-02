import tempfile

import pytest
from click.testing import CliRunner

from src.main import cli


runner = CliRunner()


@pytest.mark.parametrize(
    "template_xlsx, sheet_no, address, input_text_file, output_xlsx, expect",
    ("template1", "1", "a1", "input1", "output1", "expect"),
)
def test_cli(
    template_xlsx: str,
    sheet_no: str,
    address: str,
    input_text_file: str,
    output_xlsx: str,
    expect: str,
):
    result = runner.invoke(
        cli,
        args=[
            template_xlsx,
            "-A",
            sheet_no,
            address,
            input_text_file,
            output_xlsx,
        ],
    )
    assert result.output == "expect"
