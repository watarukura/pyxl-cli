import pandas as pd
from click.testing import CliRunner

from src.main import cli


runner = CliRunner()
e2e_test_dir = "tests/e2e/xlsx/"


def test_cli(tmpdir):
    tmp_dir_name = tmpdir.dirname

    runner.invoke(
        cli,
        args=[
            f"{e2e_test_dir}template.xlsx",
            "-T",
            1,
            "a1",
            f"{e2e_test_dir}input.csv",
            f"{tmp_dir_name}/output_from_csv.xlsx",
            "--delimiter",
            ",",
        ],
    )

    df_expected = pd.read_excel(f"{e2e_test_dir}output.xlsx", index_col=0)
    df_from_csv = pd.read_excel(
        f"{tmp_dir_name}/output_from_csv.xlsx", index_col=0
    )

    assert df_expected.equals(df_from_csv)

    runner.invoke(
        cli,
        args=[
            f"{e2e_test_dir}output.xlsx",
            "-T",
            1,
            "f6",
            f"{e2e_test_dir}input.ssv",
            f"{tmp_dir_name}/output_from_ssv.xlsx",
            "--delimiter",
            " ",
        ],
    )

    df_expected2 = pd.read_excel(f"{e2e_test_dir}output2.xlsx", index_col=0)
    df_from_ssv = pd.read_excel(
        f"{tmp_dir_name}/output_from_ssv.xlsx", index_col=0
    )

    assert df_expected2.equals(df_from_ssv)

    runner.invoke(
        cli,
        args=[
            f"{e2e_test_dir}template.xlsx",
            "-T",
            1,
            "a1",
            f"{e2e_test_dir}input.tsv",
            "-T",
            1,
            "f6",
            f"{e2e_test_dir}input.tsv",
            f"{tmp_dir_name}/output_from_tsv.xlsx",
            "--delimiter",
            "\t",
        ],
    )

    df_from_tsv = pd.read_excel(
        f"{tmp_dir_name}/output_from_tsv.xlsx", index_col=0
    )

    assert df_expected2.equals(df_from_tsv)
