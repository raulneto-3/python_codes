import xml.dom.minidom

xml_path = "python_bible/xml/file.xml"  
domtree = xml.dom.minidom.parse(xml_path)
group = domtree.documentElement
persons = group.getElementsByTagName("person")

for person in persons:
    print("*****Person*****")
    if person.hasAttribute("id"):
        print("ID:", person.getAttribute("id"))
    print("Name:", person.getElementsByTagName("name")[0].childNodes[0].data)
    print("Age:", person.getElementsByTagName("age")[0].childNodes[0].data)
    print("Weight:", person.getElementsByTagName("weight")[0].childNodes[0].data)
    print("Height:", person.getElementsByTagName("height")[0].childNodes[0].data)
    print()

# Manipulate XML
# persons = group.getElementsByTagName("person")
# persons[0].getElementsByTagName("name")[0].childNodes[0].data = "John Doe"
# domtree.writexml(open(xml_path, "w"))

# # Add new element
# new_person = domtree.createElement("person")
# new_person.setAttribute("id", "6")
# name = domtree.createElement("name")
# name.appendChild(domtree.createTextNode("Jane Doe"))
# age = domtree.createElement("age")
# age.appendChild(domtree.createTextNode("32"))
# weight = domtree.createElement("weight")
# weight.appendChild(domtree.createTextNode("70"))
# height = domtree.createElement("height")
# height.appendChild(domtree.createTextNode("170"))
# new_person.appendChild(name)
# new_person.appendChild(age)
# new_person.appendChild(weight)
# new_person.appendChild(height)
# group.appendChild(new_person)
# domtree.writexml(open(xml_path, "w"))