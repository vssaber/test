import os
import xml.etree.ElementTree as ET

tree = ET.parse(os.path.join(os.getcwd(), "config", "test02.xml"))
root = tree.getroot()

print(root.tag)
# print(root.text)

for child in root:
    print(child.tag)
    print(type(child.tag))
    print(child.attrib)
    print(type(child.attrib))

