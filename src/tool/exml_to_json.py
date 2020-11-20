import re
import os
import json

ROOT = os.path.abspath(os.path.dirname(__file__))
EXML_PATH = os.path.join(ROOT, "target.exml")
JSON_PATH = os.path.join(ROOT, "../map.py")


def main():
    with open(EXML_PATH, "r") as file:
        content = file.read()
        attrs = re.findall(r"<e:Image [\s\S]+?>", content)
        content = "MAP=" + jsonfy(attrs)

    with open(JSON_PATH, 'w') as file:
        file.write(content)
        


def jsonfy(attrs):
    result = {}
    index = 0
    for attr in attrs:
        inner_dict = {}
        split = attr.split(" ")
        for s in split:
            if "=" in s:
                key = s.split("=")[0]
                value = s.split("=")[1]
                value = value.partition('"')[2].partition('"')[0]
                inner_dict[key] = value
        result[index] = {"x": inner_dict["x"], "y": inner_dict["y"]}
        index += 1
    return json.dumps(result)


if __name__ == "__main__":
    main()