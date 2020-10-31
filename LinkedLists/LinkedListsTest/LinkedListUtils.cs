using System;
using System.Collections.Generic;
using System.Dynamic;
using System.Text;

namespace LinkedListsTest
{
    public class ListNode
    {
        private string _val;


       public ListNode(string val, ListNode next = null, ListNode prev = null)
        {
            // Constructor for ListNodeClass
            this._val = val;

            this.Next = next;
            this.Prev = prev;

        }

        public ListNode Next { get; set; }

        public ListNode Prev { get; set; }

    }

    public class DoubleLinkedList
    {

        public DoubleLinkedList()
        {
            // Constructor for DoubleLinkeList Instance
            ListNode _head = new ListNode(null, null, null);
            ListNode _tail = new ListNode(null, null, null);
            this.Head = new ListNode(null, _tail, null);
            this.Tail = new ListNode(null, null, _head); 
        }

        public ListNode Head {get; set;}

        public ListNode Tail { get; set; }

        public void PrintList()
        {
            // Print ths entire contents of the list to the command line

        }

       
    }
}
