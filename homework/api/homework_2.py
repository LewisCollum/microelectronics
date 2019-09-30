from __future__ import annotations
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
    def fromVoltage(cls, voltage):
        return Node(voltage)
        
    @classmethod
    def toBranchNode(cls, branch, node):
        return Node(node.voltage + branch.drop)

    @classmethod
    def fromNodeBranch(cls, node, branch):
        return Node(node.voltage - branch.drop)

    def __sub__(self, b):
        return self.voltage - b.voltage

class Branch:
    def __init__(self, drop):
        self.drop = drop
        self.current = None

    @classmethod
    def fromVoltage(cls, voltage):
        return Branch(voltage)

    @classmethod
    def fromNodeToNode(cls, nodeA, nodeB):
        return Branch(nodeA - nodeB)

    def swallowBranch(self, branch):
        newBranch = Branch(self.drop + branch.drop)
        if self.current != None:
            newBranch.current = self.current
        elif branch.current != None:
            newBranch.current = branch.current
        
        if branch.current == None or self.current == None:
            return newBranch
        else:
            raise RuntimeError("Currents must be the same.")

    def clearCurrent(self):
        self.current = None
        
    def __add__(self, b):
        return self.current + b.current

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __neg__(self):
        newBranch = Branch(self.drop)
        newBranch.current = -self.current
        return newBranch
    
    def setCurrentFromResistance(self, resistance):
        self.current = self.drop/resistance

    def setCurrentTowardsBranches(self, *branches):
        self.current = sum(branches)

class TestBranchAdd(unittest.TestCase):
    def setUp(self):
        self.branchA = Branch.fromVoltage(1)
        self.branchB = Branch.fromVoltage(2)
    def test_currentFromBranchA(self):
        self.branchA.current = 1

        newNode = self.branchA.swallowBranch(self.branchB)
        
        self.assertEqual(newNode.current, self.branchA.current)

    def test_currentFromBranchB(self):
        self.branchB.current = 1

        newNode = self.branchA.swallowBranch(self.branchB)

        self.assertEqual(newNode.current, self.branchB.current)        

    def test_currentIsNone(self):
        newNode = self.branchA.swallowBranch(self.branchB)

        self.assertEqual(newNode.current, None) 

    def test_currentNotSame_throwsException(self):
        self.branchA.current = 1
        self.branchB.current = 2

        self.assertRaises(RuntimeError, lambda: self.branchA.swallowBranch(self.branchB))
        
class TestBranchNode(unittest.TestCase):
    def setUp(self):
        self.branch = Branch.fromVoltage(1)
        self.node = Node.fromVoltage(1)
        
    def test_nodeFromBranchNode(self):
        newNode = Node.toBranchNode(self.branch, self.node)
        self.assertEqual(newNode.voltage, 2)

    def test_nodeToBranchNode(self):
        newNode = Node.fromNodeBranch(self.node, self.branch)
        self.assertEqual(newNode.voltage, 0)
        
    def test_branchCurrentFromResistance(self):
        self.branch.setCurrentFromResistance(1)
        self.assertEqual(self.branch.current, 1)
         
if __name__=='__main__':
    unittest.main()
