from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
            
        result = [] #[[1], [2,3]]
        queue = deque([root]) # 4,5, 6,7

        while queue:
            level = [] #2, 3
            level_nodes = len(queue) 
            for i in range(level_nodes): #i=
                node = queue.popleft() 
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            result.append(level)
        return result


        
        