from click.testing import CliRunner

from src.main import cli


runner = CliRunner()
e2e_test_dir = "tests/e2e/xlsx/"


def test_cli_csv(tmpdir):
    runner.invoke(
        cli,
        args=[
            f"{e2e_test_dir}template.xlsx",
            "-T",
            1,
            "a1",
            f"{e2e_test_dir}input.csv",
            tmpdir.join("output.xlsx"),
            "--delimiter",
            ",",
        ],
    )
    assert tmpdir.join("/output.xlsx").isfile
