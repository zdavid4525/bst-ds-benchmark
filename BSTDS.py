from __future__ import annotations

from abc import ABC


class BSTDS(ABC):
    l: BSTDS
    r: BSTDS
    x: int
    sentinel: bool


class BSTNode(BSTDS):
    def __init__(self, l=None, r=None, x=-1):
        self.left = l
        self.right = r
        self.val = x
        if x == -1:
            self.sentinel = True
        else:
            self.sentinel = False


def BSTInsert(root: BSTNode, x):
    if root.val == -1:
        root.val = x
        root.sentinel = False
        return

    if x > root.val and root.right is None:
        root.right = BSTNode(None, None, x)
    elif x < root.val and root.left is None:
        root.left = BSTNode(None, None, x)
    elif x > root.val:
        BSTInsert(root.right, x)
    elif x < root.val:
        BSTInsert(root.left, x)
    # assume all x are unique for now


def BSTDelete(root, key):
    if root is None:
        return None
    # find
    prev, curr = BSTSearch(None, root, key)
    if prev is None and curr is None:  # tree doesnt contain key
        return root
    # delete
    sucp, suc = FindSuccessor(curr)  # suc is NULL or (suc.left and suc.right is NULL)
    if prev is None:  # curr is the root
        if suc is None:
            if curr.left:
                r = curr.left
                curr.left = None
                return r
            else:
                curr.val = -1
                curr.sentinel = True
                return curr
        if curr == sucp:
            suc.left = curr.left
        else:
            suc.left, suc.right = curr.left, curr.right
        curr.left, curr.right = None, None
        return suc
    else:  # curr is not the root
        if suc is None:
            if prev.left == curr:
                prev.left = curr.left
            else:  # prev.right == curr
                prev.right = curr.left
            return root
        if curr == sucp:
            suc.left = curr.left
        else:
            suc.left, suc.right = curr.left, curr.right
        curr.left, curr.right = None, None
        if prev.left == curr:
            prev.left = suc
        else:  # prev.right == curr
            prev.right = suc
        return root


def BSTSearch(par, root, key):
    if root is None:
        return None, None
    if root.val == key:
        return par, root
    elif root.val < key:
        return BSTSearch(root, root.right, key)
    else:  # root.val > key
        return BSTSearch(root, root.left, key)


def FindSuccessor(root):
    if root.right is None:
        return root, None
    prev = root
    curr = root.right
    while curr.left is not None:
        prev = curr
        curr = curr.left
    if prev.right == curr:
        prev.right = curr.right
    else:
        prev.left = curr.right
    return prev, curr


def printInorder(root: BSTNode):
    if root is None:
        return
    printInorder(root.left)
    print(root.val)
    printInorder(root.right)


def Inorder(root: BSTNode):
    if root is None:
        return []
    A = Inorder(root.left)
    A.append(root.val)
    A.extend(Inorder(root.right))
    return A

def IsEmpty(root):
    return root.sentinel