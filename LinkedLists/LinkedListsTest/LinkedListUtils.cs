using System;
using System.Collections.Generic;
using System.Text;

namespace LinkedListsTest
{
    public class ListNode
    {

        public string _val;
        public ListNode _next;
        public ListNode _prev;

       public ListNode(string val, ListNode next = null, ListNode prev = null)
        {
            // Constructor for ListNodeClass
            this._val = val;
            this._next = next;
            this._prev = prev;
        }

    }

    public class DoubleLinkedList
    {
        private ListNode _head;

        public DoubleLinkedList()
        {
            // Constructor if given an exisitng linkined list
            this._head = new ListNode(null,null,null);
        }

        public DoubleLinkedList(ListNode exisitngNode)
        {
            // Constructor if given an exisitng linkined list
            this._head = exisitngNode;
        }

        public DoubleLinkedList (DoubleLinkedList existingList)
        {
            // Constructor if given an exisiting linked list
            this._head = existingList._head;
        }

        public void PrintList()
        {
            // Print ths entire contents of the list to the command line

        }

        public ListNode AddTail(ListNode newTail)
        {
            // Add List Node to the Tail of this Linked List
            ListNode _currNode = _head;      //
            while (_currNode._next != null)
            {
                _currNode = _currNode._next;
            }
            _currNode._next = newTail;
            newTail._prev = _currNode;
            return _head;
        }
    }
}
