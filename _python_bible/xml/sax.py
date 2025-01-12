import xml.sax

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("*****Person*****")
            print("ID:", attrs["id"])

    def endElement(self, name):
        if name == "name":
            print("Name:", self.chars)
        elif name == "age":
            print("Age:", self.chars)
        elif name == "weight":
            print("Weight:", self.chars)
        elif name == "height":
            print("Height:", self.chars)
        self.current = ""

    def characters(self, content):
        if self.current == "name":
            self.chars = content
        elif self.current == "age":
            self.chars = content
        elif self.current == "weight":
            self.chars = content
        elif self.current == "height":
            self.chars = content

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("python_bible/xml/file.xml")
