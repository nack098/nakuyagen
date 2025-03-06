import argparse

from nakuyagen.result import Result
from nakuyagen.language import Language
from nakuyagen.c import C
from nakuyagen.cpp import Cpp

project_lang: dict[str, Language] = {"c": C(), "cpp": Cpp()}

using_select = False


def args_parse(argv: list[str] | None) -> Result[str | BaseException]:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="nakuyagen",
        description="Nakuya Format Project Generator",
    )

    parser.add_argument(
        "-L", "--lang", help="Language choice", choices=project_lang.keys()
    )

    args = parser.parse_args(argv)

    if args.lang is None:
        global using_select
        using_select = True
        args.lang = [input("Select Lanugage: ").strip().lower()]

    if len(args.lang) < 1:
        return Result(
            argparse.ArgumentError(
                argument=None, message="Only one choice can be choose at a time"
            )
        )

    return Result(args.lang)


def generate(lang: str) -> None | BaseException:
    if lang not in project_lang:
        print(f"Project Language: {lang}")
        return ValueError("This language is not avalible. Please contact developer!")
    if not using_select:
        print(project_lang[lang])
    return project_lang[lang].create()


def main(argv=None) -> int:
    res = args_parse(argv).bind(generate)
    if res.is_error():
        print(res.error())
        return 1
    print("[SYSTEM]: Done!")
    return 0
