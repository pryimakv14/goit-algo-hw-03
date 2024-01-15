import argparse
from pathlib import Path
import shutil


def parse_argv():
    parser = argparse.ArgumentParser(description="Копіює файли в папку")
    parser.add_argument(
        "-s", "--source", type=Path, required=True, help="Папка з файлами"
    )
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("dist"), help="Папка для копіювання"
    )
    return parser.parse_args()


def recursive_copy(source: Path, output: Path):
    if not source.is_dir():
        print('Error: soure must be an existing directory')
        return

    for el in source.iterdir():
        if el.is_dir():
            recursive_copy(el, output)
        else:
            exttension = el.suffix
            new_path = str(el).split("/")
            new_path = Path(str(output) + "/" + exttension)
            try :
                new_path.mkdir(exist_ok=True, parents=True)
                shutil.copy(el, new_path)
            except Exception as e:
                print(e)


def main():
    args = parse_argv()
    recursive_copy(args.source, args.output)


if __name__ == "__main__":
    main()
