"Convert a valid SVG to a valid Web-Svg"

import base64
import xml.etree.ElementTree as ET

ET.register_namespace("", "http://www.w3.org/2000/svg")

mime_tipes = {"png": "image/png", "jpg": "image/jpg"}


def to_base64(file_path: str) -> str:
    "Get the data of a file in Base64 encoding"
    with open(file_path, mode="br") as file:
        out = base64.encodebytes(file.read())
    return out.decode("ascii")


def convert(input_file: str, output_file: str):
    "Convert a valid SVG to a valid Web-Svg"
    tree = ET.parse(input_file)

    for element in tree.iter():
        if "href" in element.attrib:
            f_path = element.attrib["href"]
            f_type = f_path.rpartition(".")[-1]
            f_data = to_base64(f_path)
            element.attrib["href"] = f"data:{mime_tipes[f_type]};base64,{f_data}"

    tree.write(output_file)


if __name__ == "__main__":
    convert("portafolio.svg", "readme.svg")
