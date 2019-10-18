#236p
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement

root = Element("drink")
name = SubElement(root, "name")
price = SubElement(root, "price")
cup = SubElement(root, "cup")
sugar = SubElement(root, "sugar")
ice = SubElement(root, "ice")
name.text = "하동녹차쉐이크"
price.text = "4000"
cup.text = "0"
ice.text = "3"
sugar.text="3"

ET.ElementTree(root).write("order.xml", encoding="UTF-8", xml_declaration=True)
