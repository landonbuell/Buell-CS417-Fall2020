using System;

namespace LinkedListsTest
{
    class LinkedListMain
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Double Linked List:");
            DoubleLinkedList Linked = new DoubleLinkedList("Listy");

            Linked.PrintList();

            Linked.AddHead(new ListNode("3"));

            Linked.PrintList();

            Console.WriteLine("=)");
        }
    }
}
