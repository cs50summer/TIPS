"""
You are given pointer to the root of the binary search tree and two values  and . You need to return the lowest common ancestor (LCA) of  and  in the binary search tree.

image
In the diagram above, the lowest common ancestor of the nodes  and  is the node . Node  is the lowest node which has nodes  and  as descendants.

Function Description

Complete the function lca in the editor below. It should return a pointer to the lowest common ancestor node of the two values given.

lca has the following parameters:
- root: a pointer to the root node of a binary search tree
- v1: a node.data value
- v2: a node.data value


"""





class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

        # this is a node of the tree , which contains info as data, left , right


def height(root):
    # Enter your code here

    #print(root.info)
    #print(v1)
    #print(v2)

    if root==None:
        return 0
    else:
        lheight= height(root.left)
        print("lheight",lheight)
        rheight=height(root.right)
        print("rheight",rheight)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
    #print(lvl)
    #print(max(lheight, rheight))

    #return max(lheight, rheight)



tree = BinarySearchTree()
#t = int(input())

#arr = list(map(int, input().split()))
t=6
#arr=[20,8,4,22,12,10,14]
arr = [3, 5, 2, 1, 4, 6, 7]

for i in range(t):
    tree.create(arr[i])

#v = list(map(int, input().split()))
#arr=[4,2,3,1,7,6]


ans = height(tree.root)
print(ans)
