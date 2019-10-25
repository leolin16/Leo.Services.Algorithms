using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using CsharpIntro;
using Leo.Services.Algorithms.Categories.PerformanceBenchmark;
using Microsoft.AspNetCore;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;
using BenchmarkDotNet.Running;
using Arrays;
using System.Text;
using System.Runtime.InteropServices;
using Leo.Services.Algorithms.Languages.Types.ArrayTest;
using Leo.Services.Algorithms.Languages.Types.ArrayListCustom;
using Leo.Services.Algorithms.Languages.Types.ArrayListBuiltin;
using Leo.Services.Algorithms.Categories.Search.Binary;

namespace Leo.Services.Algorithms
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // // test for basic function
            // BasicTest();

            // // performance benchmark
            // PerfTest();

            // // array test
            // ArrayCS.ArrayTest();

            // // string test
            // ArrayCS.StringTest();

            // // arraylist test
            // Console.WriteLine("This is for custom Lib List");
            // ArrayListTest.ALTest();
            // Console.WriteLine("\nThis is for builtin Lib List");
            // LiararyListTest.LibraryListTest();

            // searching algorithms(Binary + Linear)
            BinarySearchTest.BinarySearchText();
        }


        static void BasicTest()
        {

            Rectangle a = new Rectangle(1, 2);
            Rectangle b = new Rectangle(2, 4);

            Console.WriteLine($"Rectangle a area: {a.GetArea()}");
            Console.WriteLine($"Rectangle b area: {b.GetArea()}");
            Console.WriteLine($"Number of angles in a rectangle is {Rectangle.GetNumberOfAngles()}");

            Pair<int> va = new Pair<int>(1, 2);
            Pair<string> vb = new Pair<string>("1", "2");
            var vc = new List<string>(); // var means, type is defined by the statement on the right, otherwise, left and right shall be both type definition, which is a bit duplicated
        }

        static void PerfTest()
        {
            NaiveMeasurement.Measure();
            var summary = BenchmarkRunner.Run<AdvancedMeasurement>();
        }
    }
}
