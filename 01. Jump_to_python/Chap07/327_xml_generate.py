from xml.etree.ElementTree import Element,dump, SubElement, ElementTree, parse

def indent(elem, level=0):
    i = "\n"+level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i+" "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

note = Element('note')
note.attrib["date"]="20120104"
note.attrib["editor"]="pycharm"
to  = Element("to")
to.text = "Tove"
note.append(to)

SubElement(note,"to").text = "김인한"
SubElement(note,"to").text = "김기정"
SubElement(note,"to").text = "김상엽"

SubElement(note,"from").text = "Jani"

SubElement(note,"heading").text = "Reminder"
SubElement(note,"body").text = "Don't forget me this weekend!"

indent(note)
dump(note)
ElementTree(note).write("note.xml")

tree = parse("note.xml")
note = tree.getroot()

# print(note.get("date"))
# print(note.get("foo","default"))
# print(note.keys())
# print(note.items())
# to_tag = note.find("to")
# print(to_tag.text)
# to_tags = note.findall("to")
#
# for to_element in to_tags:
#     print(to_element.text)

print("Search from Root")
for parent in note.getiterator():
    for child in parent:
        print(child.text)

print("Search from from")
for child in note.getiterator("from"):
    print(child.text)


print("end")
