# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        prev = None
        node = root
        while node and node.val != key:
            prev = node
            if key < node.val:
                node = node.left
            else:
                node = node.right

        if not node:
            return root

        if not node.left or not node.right:
            child = node.left if node.left else node.right

            if not prev:
                return child

            if prev.left == node:
                prev.left = child
            else:
                prev.right = child
        else:
            succ_parent = node
            succ = node.right

            while succ.left:
                succ_parent = succ
                succ = succ.left

            node.val = succ.val

            if succ_parent == node:
                succ_parent.right = succ.right
            else:
                succ_parent.left = succ.right

        return root