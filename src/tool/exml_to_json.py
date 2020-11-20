import re
import os
import json

ROOT = os.path.abspath(os.path.dirname(__file__))
EXML_PATH = os.path.join(ROOT, "target.exml")


def main():
    with open(EXML_PATH, "r") as file:
        content = file.read()
        attrs = re.findall(r"<e:Image [\s\S]+?>", content)
        print(jsonfy(attrs))


def jsonfy(attrs):
    result = {}
    for attr in attrs:
        inner_dict = {}
        split = attr.split(" ")
        for s in split:
            if "=" in s:
                inner_dict[s.split("=")[0]] = s.split("=")[1]
        print(inner_dict)
        # result[inner_dict["name"]] = {"x": inner_dict["x"], "y": inner_dict["y"]}
    return json.dumps(result)


if __name__ == "__main__":
    main()