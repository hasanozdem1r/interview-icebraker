import os
from typing import List
import glob

CWD = os.path.dirname(__file__)


def get_md_files(directory: str = f"{CWD}/../docs") -> List[str]:
    """
    Get all md files under docs directory
    :param directory: directory to search md files, defaults to f"{CWD}/../docs"
    :return: md files path
    """
    return glob.glob(f"{directory}/*.md")


def check_duplicate_question(path: str):
    """
    Check headers to see is there any duplicate question or not
    :param path: file path
    :return: raise error
    """
    headers = []
    with open(file=path, mode="r") as file:
        for line in file:
            if line.startswith("#"):
                # clean-up header
                line = line.replace("#", "")
                headers.append(line.strip())
        duplicates = list(
            set([header for header in headers if headers.count(header) > 1])
        )
        if len(duplicates) > 0:
            raise ValueError("Duplicate question is found. Duplicate questions")
        return None


def main():
    md_files = get_md_files()
    for md_file in md_files:
        check_duplicate_question(md_file)


if __name__ == "__main__":
    main()
