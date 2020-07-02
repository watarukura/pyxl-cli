# pyxl-cli

opeypyxl wrapper for cli use.

## install

```sh
git clone https://github.com/watarukura/pyxl-cli.git .
pushd pyxl-cli
poetry install
popd
```

## usage

```sh
pyxl --help
Usage: pyxl [OPTIONS] TEMPLATE_XLSX OUTPUT_XLSX

Options:
  -T, --sheet_xy_csv <INTEGER TEXT PATH>...
                                  Sheet No and Address(ex: a1, aa12) and Input
                                  CSV file  [required]

  --delimiter TEXT                csv delimiter
  --help                          Show this message and exit.
```

for CSV file

```sh
pyxl --sheet_xy_csv 1 A1 input.csv \
    template.xlsx output.xlsx
```

for 2 TSV files

```sh
pyxl --sheet_xy_csv 1 A1 input.tsv \
    --sheet_xy_csv 1 F12 input.tsv \
    --delimiter="\t" \
    template.xlsx output.xlsx
```