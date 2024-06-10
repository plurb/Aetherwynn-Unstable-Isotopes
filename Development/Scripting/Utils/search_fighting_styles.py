import os
import sys

import re

from dotenv import dotenv_values

config = {
    **dotenv_values(".env")
}

FIGHTING_STYLES_PATH = config["FIGHTING_STYLES_PATH"]

def search(path: str, classname: str) -> list[str]:
    file_paths = [path + "/" + filename for filename in os.listdir(FIGHTING_STYLES_PATH)]
    files = dict(zip(file_paths, os.listdir(FIGHTING_STYLES_PATH)))
    
    tag_extraction_regular_expression = r"\(.*?\)"

    for p in file_paths:
        with open(p, encoding='utf-8') as f:
            tag_line = f.readlines()[1]

            # get the tags, there should only ever be one list of tags
            result_list = re.findall(tag_extraction_regular_expression, tag_line)
            if len(result_list) > 1:
                raise Exception(f"Expected one tag list, found: {len(result_list)}")
            result: str = result_list[0][1:-1]

            tags = result.split(", ")

            if classname in tags:
                yield files[p]


if __name__ == "__main__":
    print(*search(FIGHTING_STYLES_PATH, sys.argv[1]), sep='\n')
