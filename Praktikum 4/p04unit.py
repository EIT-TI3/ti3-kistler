# (c) KJR
import unittest


class Prak02Unit(unittest.TestCase):
    def testAufgabe11(self):
        import node1
        print("Test zu Aufgabe 1.1")
        n1 = node1.Node('A')
        n2 = node1.Node('B')
        n3 = node1.Node('C')
        n1.next.append(n2)
        n1.next.append(n3)
        self.assertEqual(str(n3.name), "C")
        self.assertEqual(str(n1), "A ---> B\n  ---> C")
        self.assertEqual(str(n2), "B <end>")

    def testAufgabe12(self):
        import node2
        print("Test zu Aufgabe 1.2")
        n1 = node2.Node('A')
        n2 = node2.Node('B')
        n3 = node2.Node('C')
        n1.next.append(n2)
        n1.next.append(n3)
        self.assertEqual(str(n3.name), "C")
        self.assertEqual(str(n1), "A ---> B\n  ---> C")
        self.assertEqual(str(n2), "B <end>")
        n4 = node2.Node('D')
        self.assertEqual(n4.name, "D")

    def testAufgabe13bis15(self):
        import node3
        print("Test zu Aufgabe 1.3 bis 1.5")
        n1 = node3.Node()
        n2 = node3.Node('B')
        n3 = node3.Node()
        n1.connect(n2)
        n1.connect(n3)
        self.assertEqual(str(n1), "Knoten 1 ---> B\n         ---> Knoten 3")
        self.assertEqual(str(n2), "B <end>")
        t = n1.get_connects()
        self.assertTupleEqual(t, (n2, n3))

    def testAufgabe21(self):
        import node3
        import edge
        print("Test zu Aufgabe 2.1")
        n1 = node3.Node('A')
        e1 = edge.Edge('E', 5)
        e1.connect(n1)
        self.assertEqual(str(e1), "E/5")
        e1.weight = 3
        self.assertEqual(str(e1), "E/3")

    def testAufgabe22(self):
        import node
        import edge
        print("Test zu Aufgabe 2.2")
        n1 = node.Node('A')
        n2 = node.Node('B')
        n3 = node.Node('C')
        e1 = edge.Edge('E', 5)
        e2 = edge.Edge('F', 2)
        n1.connect(e1)
        n1.connect(e2)
        e1.connect(n2)
        e2.connect(n3)
        self.assertEqual(str(n1), "A --E/5--> B\n  --F/2--> C")
        self.assertEqual(str(n2), "B <end>")

    def testAufgabe31bis32(self):
        import node
        import edge
        import graph
        print("Test zu Aufgabe 3.1 bis 3.2")
        node.Node._Node__id = 0
        g = graph.Graph()
        n1 = g.new_node('A')
        n2 = g.new_node()
        e1 = g.new_edge('E', 5)
        n1.connect(e1)
        e1.connect(n2)
        ea = g.new_edge("a", 1)
        eb = g.new_edge("b", 2)
        ec = g.new_edge("c", 3)
        self.assertEqual(str(g),
                         "Knoten:\n-------\nA --E/5--> Knoten 2\n"
                         + "Knoten 2 <end>\n\nKanten:\n-------\nE/5\n"
                         + "a/1\nb/2\nc/3\n")
        n2_new = g.find_node("Knoten 2")
        self.assertIsInstance(n2_new, node.Node)
        self.assertEqual(str(n2_new), "Knoten 2 <end>")
        eb_new = g.find_edge("b")
        self.assertIsInstance(eb_new, edge.Edge)
        self.assertEqual(str(eb_new), "b/2")
        print(e1)

    def testAufgabe33(self):
        import node
        import graph
        print("Test zu Aufgabe 3.3")
        node.Node._Node__id = 0
        g = graph.Graph()
        A = g.new_node('A')
        B = g.new_node('B')
        C = g.new_node('C')
        D = g.new_node('D')
        E = g.new_node('E')
        F = g.new_node('F')
        a = g.new_edge('a', 3)
        a.connect(B)
        b = g.new_edge('b', 7)
        b.connect(C)
        c = g.new_edge('c', 5)
        c.connect(D)
        d = g.new_edge('d', 4)
        d.connect(E)
        e = g.new_edge('e', 2)
        e.connect(A)
        f = g.new_edge('f', 1)
        f.connect(B)
        A.connect(a)
        B.connect(b)
        C.connect(c)
        C.connect(d)
        D.connect(e)
        F.connect(f)
        self.assertEqual(g.path_length(["A", "B", "C", "D", "A"]),
                         17)
        self.assertEqual(g.path_length(["A", "B", "C", "A"]),
                         -1)
        self.assertEqual(g.path_length(["A", "B", "C", "E"]),
                         14)

    def testAufgabe41bis42(self):
        import reader
        print("Test zu Aufgabe 4.1 bis 4.2")
        r1 = reader.Reader()
        g1 = r1.read("C:/Users/Martin/LRZ Sync+Share/Workspace/GitHub/TI3-Prog-Ressel/Praktikum 4/Karte.xml")
        s = str(g1)
        self.assertTrue("inzerer" in s)
        self.assertTrue("rresstr" in s)
        self.assertTrue("othstr" in s)
        self.assertTrue("chelling" in s)
        self.assertTrue("ranach" in s)
        self.assertTrue("eor" in s)

        node1, node2 = '295170', '1954408'
        path, dist = g1.find_path(node1, node2)

        print("-"*50)
        print("Found Path from:")
        print(f"Node {node1}: https://www.openstreetmap.org/node/{node1}")
        print("to")
        print(f"Node {node2}: https://www.openstreetmap.org/node/{node2}")
        print("-"*50)
        print(f"Total distance: {dist}m")
        print("Path:")
        print("".join(node + '\n' for node in path))


if __name__ == "__main__":
    unittest.main()
