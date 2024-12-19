import unittest
from random import randint

from BSTDS import BSTNode, BSTInsert, Inorder, FindSuccessor
from RandomizedSet import RandomizedSet


class BSTTest(unittest.TestCase):
    def test_BSTInsert(self):
        T = BSTNode()
        r = randint(0, 1000)
        RS = RandomizedSet()
        for i in range(r):
            RS.insert(i)
        while not RS.isEmpty():
            v = RS.getRandom()
            RS.remove(v)
            BSTInsert(T, v)
        assert (Inorder(T) == list(range(r)))

    def test_BSTSuccessorIntegrity(self):
        T = BSTNode()
        r = randint(0, 100000)
        RS = RandomizedSet()
        for i in range(r):
            RS.insert(i)
        while not RS.isEmpty():
            v = RS.getRandom()
            RS.remove(v)
            BSTInsert(T, v)
        A = Inorder(T)
        s = FindSuccessor(T)[1]
        if s is not None:
            A.remove(s.val)
            assert (A == Inorder(T))
        else:
            assert (T.val == r - 1)

if __name__ == '__main__':
    unittest.main()
