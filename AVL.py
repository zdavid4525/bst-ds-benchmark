from __future__ import annotations


class AVLNode:
    left: AVLNode
    right: AVLNode
    val: int
    height: int
    sentinel: bool

    def __init__(self,val=-1):
        if val == -1:
            self.left, self.right = self, self
            self.height=-1
            self.sentinel=True
        else:
            self.left, self.right = AVLNode(), AVLNode()
            self.height=0
            self.sentinel = False
        self.val=val


def AVLInsert(T, v):
    if IsEmpty(T):
        T.val = v
        T.sentinel = False
        T.left, T.right = AVLNode(), AVLNode()
        T.height = 0
        return T
    elif T.val < v:
        T.right = AVLInsert(T.right,v)
    else:
        T.left = AVLInsert(T.left,v)
    T.height = max(T.left.height + 1, T.right.height + 1)
    return AVLRebalance(T)


def AVLRebalance(T):
    BF = T.left.height - T.right.height
    if BF > 1:  # left heavy
        if T.left.left.height > T.left.right.height:
            # right zig
            x, y, z = T, T.left, T.left.left
            x.left = y.right
            x.height = max(x.left.height+1,x.right.height+1)
            y.right = x
            y.height = max(y.left.height+1, y.right.height+1)
            return y
        else:
            # left zig
            x, y, z = T, T.left, T.left.right
            y.right = z.left
            y.height = max(y.left.height+1, y.right.height+1)
            z.left = y
            z.height = max(z.left.height+1, z.right.height+1)
            x.left = z
            x.height = max(x.left.height+1, x.right.height+1)
            # right zag
            x.left = z.right
            x.height = max(x.left.height+1, x.right.height+1)
            z.right = x
            z.height = max(z.left.height+1, z.right.height+1)
            return z
    elif BF < -1:  # right heavy
        if T.right.left.height > T.right.right.height:
            # right zig
            x, y, z = T, T.right, T.right.left
            y.left = z.right
            y.height = max(y.left.height + 1, y.right.height + 1)
            z.right = y
            z.height = max(z.left.height + 1, z.right.height + 1)
            x.right = z
            x.height = max(x.left.height + 1, x.right.height + 1)
            # left zag
            x.right = z.left
            x.height = max(x.left.height + 1, x.right.height + 1)
            z.left = x
            z.height = max(z.left.height + 1, z.right.height + 1)
            return z
        else:
            # left zig
            x, y, z = T, T.right, T.right.right
            x.right = y.left
            x.height = max(x.left.height + 1, x.right.height + 1)
            y.left = x
            y.height = max(y.left.height + 1, y.right.height + 1)
            return y
    return T

def _AVLSearch(P, T, v):
    if IsEmpty(T):
        return T, T
    if T.val == v:
        return P, T
    elif T.val < v:
        return _AVLSearch(T, T.right, v)
    else:
        return _AVLSearch(T, T.left, v)


def AVLSearch(T, v):
    if IsEmpty(T):
        return T
    if T.val == v:
        return T
    elif T.val < v:
        return AVLSearch(T.right, v)
    else:
        return AVLSearch(T.left, v)


def IsEmpty(T):
    return T.sentinel

def printInorder(root):
    if IsEmpty(root):
        return
    printInorder(root.left)
    print(root.val)
    printInorder(root.right)


def AVLInorder(root):
    if IsEmpty(root):
        return []
    A = AVLInorder(root.left)
    A.append(root.val)
    A.extend(AVLInorder(root.right))
    return A
