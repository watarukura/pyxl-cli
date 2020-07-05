import pytest
from click.testing import CliRunner

from src.main import read, write


runner = CliRunner()
e2e_test_dir = "tests/e2e/xlsx/"


@pytest.mark.parametrize(
    "template_xlsx, sheet_no, xy, input_csv, delimiter, output_xlsx",
    (("template.xlsx", "1", "A1", "input.csv", None, "output.xlsx",),),
)
def test_cli(
    template_xlsx: str,
    sheet_no: str,
    xy: str,
    input_csv: str,
    delimiter: str,
    output_xlsx: str,
    tmpdir,
):
    tmp_dir_name = tmpdir.dirname

    runner.invoke(
        write,
        args=[
            f"{e2e_test_dir}{template_xlsx}",
            "-T",
            sheet_no,
            xy,
            f"{e2e_test_dir}{input_csv}",
            f"{tmp_dir_name}/{output_xlsx}",
            "--delimiter",
            delimiter,
        ],
    )

    result = runner.invoke(
        read,
        args=[
            f"{tmp_dir_name}/{output_xlsx}",
            "--sheet_no",
            sheet_no,
            "--delimiter",
            delimiter,
        ],
    )

    result_expected = runner.invoke(
        read,
        args=[
            f"{e2e_test_dir}/{output_xlsx}",
            "--sheet_no",
            sheet_no,
            "--delimiter",
            delimiter,
        ],
    )

    assert result.output == result_expected.output
