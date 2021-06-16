from graph import Graph

class Reader:

    def __init__(self):
        self.g = Graph()

    def read(self, filename):
        import xml.etree.ElementTree as ET
        tree = ET.parse(filename)
        root = tree.getroot()
        for child in root:
            if child.tag.lower()=='node':
                try:
                    name = child.attrib['name']
                except:
                    name = None
                self.g.new_node(name)
            elif child.tag.lower()=='edge':
                try:
                    self.g.new_edge(child.attrib['name'], int(child.attrib['weight']))
                except:
                    print('Fehler in Edge-Knoten')

        root = tree.getroot()
        for child in root:
            if child.tag.lower()=='node':
                curr_node = self.g.find_node(child.attrib['name'])
                for grandchild in child:
                    if grandchild.tag.lower()=='next':
                        e = self.g.find_edge(grandchild.text)
                        curr_node.connect(e)
            elif child.tag.lower()=='edge':
                curr_edge = self.g.find_edge(child.attrib['name'])
                for grandchild in child:
                    if grandchild.tag.lower()=='next':
                        n = self.g.find_node(grandchild.text)
                        curr_edge.connect(n)

        return self.g


