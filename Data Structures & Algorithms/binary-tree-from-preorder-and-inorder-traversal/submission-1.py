# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            root = TreeNode(preorder[self.pre_idx])
            mid = inorder_map[root.val]
            self.pre_idx += 1

            root.left  = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        # if not preorder or not inorder:
        #     return None

        # # preorder: [5, 4, 9, 6, 3, 7]
        # # inorder : [9, 4, 5, 3, 6, 7]
        # root = TreeNode(preorder[0])
        # mid = inorder.index(root.val)

        # root.left  = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return build(0, n - 1)