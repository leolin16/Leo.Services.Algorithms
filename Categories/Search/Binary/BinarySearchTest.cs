using System;
using Arrays;
using Leo.Services.Algorithms.Categories.Search.Linear;

namespace Leo.Services.Algorithms.Categories.Search.Binary
{
    public class BinarySearchTest
    {
        public static void BinarySearchText()
        {
            int[] testArray =
                new int[] { -34, -21, -18, -12, -3, -1, 0, 3, 8, 12, 23 }; // sorted for binary usage, for linear search, no need to be sorted

            Console.Write($"Test array: ");
            testArray.PrintElements();

            int testItem = -12;
            PrintSearchInformation(testItem, testArray);

            testItem = 0;
            PrintSearchInformation(testItem, testArray);

            testItem = 23;
            PrintSearchInformation(testItem, testArray);

            testItem = 2;
            PrintSearchInformation(testItem, testArray);
        }
        static void PrintSearchInformation(int testItem, int[] testArray)
        {
            Console.WriteLine($"Searching for {testItem}: " +
                $"Linear {testArray.LinearSearch(testItem)}, " +
                $"Binary {testArray.BinarySearchRecursive(testItem)}, " +
                $"Binary iterative {testArray.BinarySearchIterative(testItem)}");
        }
    }
}