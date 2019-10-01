using System;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using Arrays;

namespace Leo.Services.Algorithms.Languages.Types.ArrayTest
{
    public class ArrayCS
    {

        public static void StringTest()
        {
            string message = "Hello, World!";

            // string is an array of chars
            for(int i = 0; i < message.Length; i ++)
            {
                if(i > 6 && i < 12)
                {
                    Console.Write(message[i]);
                }
            }
            Console.WriteLine();

            // but we cannot change strings in C# in this way
            // message[7] = 'w';

            message = "The number to be parsed is: 123";
            // this creates a new string
            // Substring, Trim, IsNullOrWhitespace will also produce more strings
            string num = message.Substring(message.IndexOf(':') + 2);
            int.TryParse(num, out var a);
            Console.WriteLine(a);

            // this does not create string copies
            ReadOnlySpan<char> msgSpan = message;
            ReadOnlySpan<char> numSpan = msgSpan.Slice(msgSpan.IndexOf(':') + 2);
            int.TryParse(numSpan, out var b);
            Console.WriteLine(b);

            string firstString = "Test string";
            string secondString = "Test string";

            // Prints out true, because of sting intern pool
            Console.WriteLine(object.ReferenceEquals(firstString, secondString));

            // The following is not possible, the api gives
            // only ReadOnlySpan and ReadOnlyMemory
            // Span<char> span = firstString.AsSpan();
            // Memory<char> mem = firstString.AsMemory();

            // Only use this approach when you know what you're doing
            // and aware of the consequences
            Memory<char> mem = MemoryMarshal.AsMemory(firstString.AsMemory());
            mem.Span[5] = 'Z';

            Console.WriteLine(firstString);
            Console.WriteLine(secondString);

            // Use stringbuilder or memory buffers if you need
            // to concatenate lots of strings

            var sb = new StringBuilder();
            foreach(int i in Enumerable.Range(1,10))
            {
                sb.Append(i.ToString());
            }

            Console.WriteLine(sb.ToString());
        }

        // will need extension.cs to give extended methods on asrray like PrintElements
        static void ArrayTest()
        {
            int[] array = new int[] { 1, 2, 3 };

            array.PrintElements();
            array[1] = 10;
            array.PrintElements();

            try
            {
                array[3] = 10;
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }

            // A multi-dimensional array. 2D space,
            // a table in this case
            int[,] a = {
                { 1, 2, 3},
                { 4, 5, 6}
            };
            Console.WriteLine(
                $"A multi-dimensional array length: {a.Length}");
            Console.WriteLine(
                $"The 2,3 position element is : {a[1,2]}");

            // A jagged array. It's an array of arrays, so you
            // need to initialize nested arrays afterwards
            int[][] b =  {
                new int[] { 1, 2, 3 },
                new int[] { 10, 20, 30, 40, 50 },
                new int[] { 5, 6 },
            };

            Console.WriteLine($"The jagged array length: {b.Length}");
            Console.WriteLine($"The nested array length: {b[1].Length}");

            // an element in the first row, first column
            a[0, 0] = 10;

            // The first element's first element
            b[0][0] = 10;

            int[][][] c = new int[2][][];
            // int[2][2][2] or int[2][2][] is not possible -
            // you can initialize only the first rank
            // Also, nested arrays are not initialized,
            // c[0].Length will give null reference exception
        }
    }
}