/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
         helper(root);
         return true;
    }

    private void helper(TreeNode root){
        if (root == null) return;
      
        helper(root.left);
        
        helper(root.right);
    }
  
}

// T(C): O(n) i.e. number of nodes
// S(C): O(h) height of recursive stack
