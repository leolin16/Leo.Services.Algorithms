using System;
using System.Collections.Generic;
using System.Text;
using Leo.Services.Algorithms.Languages.Types.ArrayListCustom;

namespace Arrays
{
    public static class Extensions
    {
        public static void PrintElements<T>(this T[] array)
        {
            if (null == array || array.Length == 0)
            {
                Console.WriteLine("[]");
                return;
            }

            Console.Write("[");
            for (int i = 0; i < array.Length; i++)
            {
                if (i == 0)
                {
                    Console.Write($"{array[i]}");
                }
                else
                {
                    Console.Write($", {array[i]}");
                }
            }
            Console.WriteLine("]");
        }

        public static void PrintElements<T>(this List<T> arrayList)
        {
            if (null == arrayList || arrayList.Count == 0)
            {
                Console.WriteLine("[]");
                return;
            }

            Console.Write("[");
            for (int i = 0; i < arrayList.Count; i++)
            {
                if (i == 0)
                {
                    Console.Write($"{arrayList[i]}");
                }
                else
                {
                    Console.Write($", {arrayList[i]}");
                }
            }
            Console.WriteLine("]");
        }

        public static void PrintElements<T>(this ArrayList<T> arrayList)
        {
            if (null == arrayList || arrayList.Length == 0)
            {
                Console.WriteLine("[]");
                return;
            }

            Console.Write("[");
            for (int i = 0; i < arrayList.Length; i++)
            {
                if (i == 0)
                {
                    Console.Write($"{arrayList[i]}");
                }
                else
                {
                    Console.Write($", {arrayList[i]}");
                }
            }
            Console.WriteLine($"], storageSize: {arrayList.StorageLength}");
        }

        public static void Swap<T>(this T[] array, int i, int j)
        {
            if (i < 0 || i >= array.Length) throw new ArgumentOutOfRangeException(nameof(i));
            if (j < 0 || j >= array.Length) throw new ArgumentOutOfRangeException(nameof(j));


            T temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }

        public static T[] CreateCopy<T>(this T[] sourceArray)
        {
            T[] array = new T[sourceArray.Length];
            sourceArray.CopyTo(array, 0);

            return array;
        }
    }
}
