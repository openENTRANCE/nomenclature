import pathlib
import yaml


def test_parse_yaml_files():
    # check that all yaml files can be parsed without errors

    # iterate over the yaml files in all sub-folders and try loading
    lst = []
    for file in pathlib.Path('.').glob('**/*.yaml'):
        try:
            with open(file, 'r') as stream:
                yaml.safe_load(stream)
        except (yaml.scanner.ScannerError, yaml.parser.ParserError) as e:
            lst.append(file)
            print(f"Error parsing file `{file}`\n{e}\n")

    # tests fails if any file cannot be parsed
    assert not lst