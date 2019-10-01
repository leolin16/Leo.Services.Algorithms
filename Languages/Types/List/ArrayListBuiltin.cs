using System;
using System.Collections.Generic;
using Arrays;

namespace Leo.Services.Algorithms.Languages.Types.ArrayListBuiltin
{
    public class LiararyListTest
    {
        public static void LibraryListTest()
        {
            List<int> arrayList = new List<int> { 4, 5, 6 };
            arrayList.PrintElements();
            try
            {
                arrayList[3] = 20;
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            arrayList.Add(20);
            arrayList.PrintElements();
            arrayList.Insert(2, 200);
            arrayList.PrintElements();
        }
    }
}