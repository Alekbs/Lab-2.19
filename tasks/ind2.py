#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import pathlib
import json
import colorama
from colorama import Fore, Style


def tree(directory):
    """
    Создание древа файлов
    """
    str = ""
    for path in sorted(directory.rglob("*")):
        depth = len(path.relative_to(directory).parts)
        spacer = " " * depth
        print(f"Это проверка: {path.name}")
        if path
        str += Fore.BLUE + Style.BRIGHT + f"{spacer} >> {path.name}\n"
        for new_path in sorted(directory.joinpath(path).glob("*")):
            depth = len(new_path.relative_to(directory.joinpath(path)).parts)
            spacer = "\t" * depth
            str += Fore.BLUE + f"{spacer} > {new_path.name}\n"
    return str


def size(filename):
    """
    Получение размера файла
    """
    sez = pathlib.Path(filename).stat().st_size
    return sez


def save(filename, lost):
    """
    Сохранить список поездов в json-файл
    """
    # Открыть файл с заданным именем для записи.
    with open(filename, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кирилицы установим ensure_ascii=False
        json.dump(lost, fout, ensure_ascii=False, indent=4)


def help():
    print("all - просмотр полного пути файла")
    print("files - просмотр всех файлов в директории")
    print("seze - просмотр размера файла")
    print("save - сохранение данных в json-файл")
    print("mkdir - создание дириктории")
    print("rmdir - удаление дириктории")
    print("mk - создание файла")
    print("rm - удаление файла")


def main(command_line=None):
    colorama.init()
    current = pathlib.Path.cwd()
    file_parser = argparse.ArgumentParser(add_help=False)

    # Создаем основной парсер командной строки
    parser = argparse.ArgumentParser("tree")
    parser.add_argument(
        "--version", action="version", help="The main parser", version="%(prog)s 0.1.0"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Создаем субпарсер для создания новой папки
    create = subparsers.add_parser("mkdir", parents=[file_parser])
    create.add_argument("filename", action="store")

    # Субпарсер для удаления папок
    create = subparsers.add_parser("rmdir", parents=[file_parser])
    create.add_argument("filename", action="store")

    # Субпарсер для создания файлов
    create = subparsers.add_parser("mk", parents=[file_parser])
    create.add_argument("filename", action="store")
    # Субпарсер для удаления файлов
    create = subparsers.add_parser("rm", parents=[file_parser])
    create.add_argument("filename", action="store")

    # Субпарсер для вывода help-строки
    create = subparsers.add_parser("help", parents=[file_parser])

    # Субпарсер для вывода всех файлов дириктории
    create = subparsers.add_parser("files", parents=[file_parser])

    # Субпарсер для вывода дирикторий
    create = subparsers.add_parser("dir", parents=[file_parser])

    # Субпарсер для вывода полного пути
    create = subparsers.add_parser("all", parents=[file_parser])

    # save
    create = subparsers.add_parser("save", parents=[file_parser])
    create.add_argument("filename", action="store")
    args = parser.parse_args(command_line)
    if args.command == "mkdir":
        directory_path = current / args.filename
        directory_path.mkdir()
        tree(current)
    elif args.command == "rmdir":
        directory_path = current / args.filename
        directory_path.rmdir()
        tree(current)
    elif args.command == "mk":
        directory_path = current / args.filename
        directory_path.touch()
        tree(current)
    elif args.command == "rm":
        directory_path = current / args.filename
        directory_path.unlink()
        tree(current)
    elif args.command == "all":
        print(Fore.RED + f"{current}")
    elif args.command == "help":
        help()
    elif args.command == "files":
        print(tree(current))
    elif args.command == "save":
        save(args.filename, tree(current))
    elif args.command == "dir":
        p = pathlib.Path('.')
        current = [print(x) for x in p.iterdir() if x.is_dir()]
    else:
        print('Введите"help" для вывода списка комманд')


if __name__ == "__main__":
    main()
