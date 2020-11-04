using System;
using System.Collections.Generic;
using System.Text;

namespace LinkedTree
{
    public class TreeNode
    {
        
        public TreeNode(string _val, 
            List<TreeNode> _next = null, List<TreeNode> _prev = null)
        {
            // Constructor Method for TreeNode Class
            this.Data = _val;
            this.Next = _next;
            this.Prev = _prev;
        }

        public string Data { get; set; }

        public List<TreeNode> Next { get; set; }

        public List<TreeNode> Prev { get; set; }

        public List<TreeNode> AddNext (TreeNode _newNode)
        {
            // Add new Node to "next" field
            Next.Add(_newNode);
            return Next;
        }

        public List<TreeNode> AddPrev (TreeNode _newNode)
        {
            // Add new Node to "prev" field
            Prev.Add(_newNode);
            return Prev;
        }
    }
}
