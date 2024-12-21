import unittest
from random import randint

from AVL import AVLNode, AVLInsert, printInorder
from RandomizedSet import RandomizedSet


class AVLTest(unittest.TestCase):
    def test_BSTInsert(self):
        T = AVLNode()
        T = AVLInsert(T, 1)
        T = AVLInsert(T,2)
        T = AVLInsert(T,3)
        printInorder(T)
        # r = randint(0, 100000)
        # RS = RandomizedSet()
        # for i in range(r):
        #     RS.insert(i)
        # while not RS.isEmpty():
        #     v = RS.getRandom()
        #     RS.remove(v)
        #     AVLInsert(T, v)
        # assert (Inorder(T) == list(range(r)))

    # def test_BSTDelete(self):
    #     T = BSTNode()
    #     r = randint(0, 100000)
    #     RS1 = RandomizedSet()
    #     RS2 = RandomizedSet()
    #     for i in range(r):
    #         RS1.insert(i)
    #         RS2.insert(i)
    #     while not RS1.isEmpty():
    #         v = RS1.getRandom()
    #         RS1.remove(v)
    #         BSTInsert(T, v)
    #     while not IsEmpty(T):
    #         v = RS2.getRandom()
    #         RS2.remove(v)
    #         T=BSTDelete(T, v)
    #     assert(IsEmpty(T))

    # def test_BSTSearch(self):
    #     T = BSTNode()
    #     r = randint(0, 100000)
    #     RS1 = RandomizedSet()
    #     RS2 = RandomizedSet()
    #     for i in range(r):
    #         RS1.insert(i)
    #         RS2.insert(i)
    #     while not RS1.isEmpty():
    #         v = RS1.getRandom()
    #         RS1.remove(v)
    #         BSTInsert(T, v)
    #     while not RS2.isEmpty():
    #         v = RS2.getRandom()
    #         RS2.remove(v)
    #         _,n=BSTSearch(None, T, v)
    #         assert(n.val == v)

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
