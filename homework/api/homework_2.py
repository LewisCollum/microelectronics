import pint
import unittest

unit = pint.UnitRegistry()

def printEquation(tag, value, digits):
    print(f"\\noindent\\[{tag} = {value:.{digits}Lx}\\]")

def printBoxedEquation(tag, value, digits):
    print("\\noindent\\[\\boxed{", f"{tag} = {value:.{digits}Lx}", "}\\]")


class Node:
    def __init__(self, voltage):
        self.voltage = voltage

    @classmethod
    def fromBranchNode(cls, branch, node):
        return Node(node.voltage + branch.drop)

    @classmethod
    def toBranchNode(cls, node, branch):
        return Node(node.voltage - branch.drop)

class Branch:
    def __init__(self, drop):
        self.drop = drop


class TestBranchNode(unittest.TestCase):
    def test_nodeFromBranchNode(self):
        branch = Branch(1)
        node =  Node(1)
        newNode = Node.fromBranchNode(branch, node)

        self.assertEqual(newNode.voltage, 2)

    def test_nodeToBranchNode(self):
        branch = Branch(1)
        node =  Node(1)
        newNode = Node.toBranchNode(node, branch)

        self.assertEqual(newNode.voltage, 0)
        

if __name__=='__main__':
    unittest.main()
