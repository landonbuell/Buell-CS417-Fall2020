using System;

namespace LinkedListsTest
{
    class LinkedListMain
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            ListNode HeadNode = new ListNode("3", null, null);
            DoubleLinkedList Linked = new DoubleLinkedList();

            Linked.AddTail(new ListNode("3"));

            Console.WriteLine("=)");
        }
    }
}
