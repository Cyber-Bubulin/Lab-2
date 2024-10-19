import xml.dom.minidom as minidom


if __name__ == "__main__":
    data = open('currency.xml')
    xml_file = data.read()


    dom = minidom.parseString(xml_file)
    dom.normalize()

    elements = dom.getElementsByTagName('Valute')
    currency_dict={}

    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Nominal':
                    if child.firstChild.nodeType == 3:
                        value = child.firstChild.data.replace(',','.')
                if child.tagName == "CharCode":
                    if child.firstChild.nodeType == 3:
                        char_code = child.firstChild.data
        currency_dict[char_code] = value



    print(currency_dict)