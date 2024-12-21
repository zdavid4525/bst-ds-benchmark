import time
import sys
import unittest
from random import randint

from AVL import AVLNode, AVLInsert, AVLInorder, AVLSearch
from UBBST import BSTNode, BSTInsert, Inorder, FindSuccessor, BSTDelete, IsEmpty, BSTSearch
from RandomizedSet import RandomizedSet


class BSTTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = randint(0, 10000)
        sys.setrecursionlimit(cls.r+20)
        cls.A1=[]
        cls.A2=[]
        cls.A3=[]
        for i in range(cls.r):
            cls.A1.append(i)
            cls.A2.append(cls.r-i-1)
            if i % 2 == 0:
                cls.A3.append(i)
            else:
                cls.A3.append(cls.r-i-1)

    def test_Insert(cls):
        s = time.time()
        T = BSTNode()
        for v in cls.A1:
            BSTInsert(T, v)
        e = time.time()
        print("Unbalanced BST Worst Case INSERT: ",e-s)
        assert (Inorder(T) == list(range(cls.r)))

        s = time.time()
        T = AVLNode()
        for v in cls.A1:
            T = AVLInsert(T, v)
        e = time.time()
        print("AVL Worst Case INSERT: ",e-s)
        assert (AVLInorder(T) == list(range(cls.r)))  # on average, >100x faster than Unbalanced BST Insert.
        # INSERT cost can be improved by mutating tree directly


    # def test_BSTDelete(cls):
    #     T = BSTNode()
    #     for v in cls.A1:
    #         BSTInsert(T, v)
    #     for v in cls.A2:
    #         T=BSTDelete(T, v)
    #     assert(IsEmpty(T))

    def test_Search(cls):
        T = BSTNode()
        for v in cls.A1:
            BSTInsert(T, v)
        s = time.time()
        for v in cls.A2:
            n=BSTSearch(T, v)
            assert(n.val == v)
        e = time.time()
        print("Unbalanced BST Random Uniform SEARCH: ", e-s)

        T = AVLNode()
        for v in cls.A1:
            T = AVLInsert(T, v)
        s = time.time()
        for v in cls.A2:
            n=AVLSearch(T, v)
            assert(n.val == v)
        e = time.time()
        print("AVL Random Uniform SEARCH: ", e-s)  # massive (>2000) increase in performance vs Unbalanced BST


    # def test_BSTSuccessorIntegrity(self):
    #     T = BSTNode()
    #     r = randint(0, 100000)
    #     RS = RandomizedSet()
    #     for i in range(r):
    #         RS.insert(i)
    #     while not RS.isEmpty():
    #         v = RS.getRandom()
    #         RS.remove(v)
    #         BSTInsert(T, v)
    #     A = Inorder(T)
    #     s = FindSuccessor(T)[1]
    #     if s is not None:
    #         A.remove(s.val)
    #         assert (A == Inorder(T))
    #     else:
    #         assert (T.val == r - 1)

if __name__ == '__main__':
    unittest.main()
