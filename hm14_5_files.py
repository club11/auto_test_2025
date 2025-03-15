"""Homework 14 - 5. XML"""

import xml.etree.ElementTree as Et


def task_five():
    """
    XML
    """
    root = Et.Element("data")
    doc = Et.SubElement(root, "product")
    Et.SubElement(doc, "description", name="description").text = "cellphone"
    Et.SubElement(doc, "price", name="price").text = "100"
    Et.SubElement(doc, "currency", name="price").text = "USD"
    doc = Et.SubElement(root, "product")
    Et.SubElement(doc, "description", name="description").text = "cellphone2"
    Et.SubElement(doc, "price", name="price").text = "200"
    Et.SubElement(doc, "currency", name="price").text = "USD"
    tree = Et.ElementTree(root)
    tree.write("not_best_choice.xml")

    def parse_xml(xml_str):
        """
        work with xml file
        """
        tree_is = Et.parse(xml_str)
        root_is = tree_is.getroot()
        total_cost = 0
        for child in root_is.findall('product'):
            # product = child.find('description').text
            price = child.find('price').text
            # currency = child.find('currency').text
            total_cost += (int(price))
        return print('total_cost =', total_cost)

    return parse_xml("not_best_choice.xml")


if __name__ == "__main__":
    task_five()
