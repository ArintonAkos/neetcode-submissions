# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"

        return f"{root.val}#{self.serialize(root.left)}#{self.serialize(root.right)}"
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = iter(data.split("#"))

        def dfs() -> Optional[TreeNode]:
            curr = next(vals)

            if curr == "N":
                return None

            curr_val = int(curr)
            root = TreeNode(curr_val)
            root.left  = dfs()
            root.right = dfs()

            return root

        return dfs()