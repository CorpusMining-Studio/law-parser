import re
import os
import json


DATA_DIR = "ROC-Laws-and-Regulations"
OUTPUT_DIR = "output"


def process_md(content):
    articles = re.findall(
        r"(### \*\*第 [\d\-]+ 條\*\*)\n\n(.*?)\n(?=(###|\Z))", content, re.S
    )
    return [f"{article[0]}\n{article[1].strip()}" for article in articles]


def output(data, filename):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    with open(OUTPUT_DIR + f"/{filename}", "w", encoding="utf-8") as f:
        json.dump({"articles": data}, f, ensure_ascii=False, indent=4)
    return


def main():
    for dirpath, _, filenames in os.walk(DATA_DIR):
        for file in filenames:
            if file.endswith(".md"):
                with open(os.path.join(dirpath, file), "r") as f:
                    content = f.read()
                    articles = process_md(content)
                    output(articles, file.replace(".md", ".json"))
    return


if __name__ == "__main__":
    main()
