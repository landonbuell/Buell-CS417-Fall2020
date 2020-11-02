using System;
using System.Collections.Generic;
using System.Dynamic;
using System.Reflection.Metadata.Ecma335;
using System.Text;

namespace LinkedListsTest
{
    public class ListNode
    {

        public ListNode(string strVal, ListNode next = null, ListNode prev = null)
        {
            // Constructor for ListNode Class containing string
            this.Data = strVal;
            this.Next = next;
            this.Prev = prev;
        }

        public ListNode Next { get; set; }

        public ListNode Prev { get; set; }

        public string Data { get; set; }

    }

    public class DoubleLinkedList
    {
        private string listName;

        public DoubleLinkedList(string name = " ")
        {
            // Constructor for DoubleLinkeList Instance
            listName = name;
            Head = new ListNode(null, null, null);
            Tail = new ListNode(null, null, null);

            Head.Next = Tail;
            Tail.Prev = Head; 
        }

        public ListNode Head {get; set;}

        public ListNode Tail { get; set; }

        private int ListLength()
        {
            // Get the number of Nodes in this List Instance
            int _count = 0;
            ListNode _currNode = Head.Next;
            while (_currNode.Next != Tail)
            {
                _count += 1;
                _currNode = _currNode.Next;
            }
            return _count;
        }

        public int GetLength() { return ListLength();}

        public ListNode AddHead (ListNode _newHead)
        {
            // Add Node to Head of Linked List
            ListNode _currHead = Head.Next;
            _currHead.Prev = _newHead;
            _newHead.Next = _currHead;
            _newHead.Prev = Head;
            Head.Next = _newHead;
            return Head;
        }

        public ListNode AddTail (ListNode _newTail)
        {
            // Add Node to Tail of Linked list
            ListNode _currTail = Tail.Prev;
            _currTail.Next = _newTail;
            _newTail.Prev = _currTail;
            _newTail.Next = Tail;
            Tail.Prev = _newTail;
            return Head;
        }

        public void PrintList()
        {
            // Print ths entire contents of the list to the command line
            Console.WriteLine("DoubleLinkedList Instance Name:", listName);
            ListNode _currNode = Head.Next;
            Console.Write("{0:-8} ->", "Head Node");
            while (_currNode.Next != Tail)
            {
                // Iterate through List
                Console.Write("{0:-8} ->", _currNode.Data);
                _currNode = _currNode.Next;
            }
            Console.Write("{0:-8} ->", "Tail Node");

        }



       
    }
}
