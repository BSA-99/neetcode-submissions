# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            lev_nodes = len(queue)

            for i in range(lev_nodes):
                node = queue.popleft()
                if i == (lev_nodes-1):
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
                
        