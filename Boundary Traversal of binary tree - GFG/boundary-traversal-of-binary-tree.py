#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # def printBoundaryView(self, root):
    def left_traversal(self,root,ans):
        # or in bracket is for jiske bache nahi hai
        if root is None or (root.left is None and root.right is None):
            return
        # phele append karo data kyu ki correct order jarahe
        ans.append(root.data)
        if root.left:
            self.left_traversal(root.left,ans)
        else:
            self.left_traversal(root.right,ans)
    def leaf_traversal(self,root,ans):
        if root is None:
            return
        # kya mere baache hai. nahi toh add karo
        if root.left is None and root.right is None:
            ans.append(root.data)
            return
        self.leaf_traversal(root.left,ans)
        self.leaf_traversal(root.right,ans)
    def right_traversal(self,root,ans):
        if root is None or (root.left is None and root.right is None):
            return
        # right traversal kar raha isleye sabase phele right maih jaa raha
        if root.right:
            self.right_traversal(root.right,ans)
        else:
            self.right_traversal(root.left,ans)
        # wapas aate samay insert kyu ki hamme reverse order maih jaanaa hai
        ans.append(root.data) 
    def printBoundaryView(self, root):
        # Code here
        if root is None:
            return
        ans=[]
        ans.append(root.data)
        # left subtree traversal
        self.left_traversal(root.left,ans)
        # leaf node
        # leaf node for leftsubtree
        self.leaf_traversal(root.left,ans)
        # leaf node for rightsubtree
        self.leaf_traversal(root.right,ans)
        # right side traversal
        self.right_traversal(root.right,ans)
        return ans
        # Code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
#{ 
#  Driver Code Starts
import sys

import sys
sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        obj = Solution()
        res = obj.printBoundaryView(root)
        for i in res:
            print (i, end = " ")
        print('')
# } Driver Code Ends