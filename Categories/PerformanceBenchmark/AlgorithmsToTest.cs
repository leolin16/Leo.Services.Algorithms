using System;
using System.Threading;
namespace Leo.Services.Algorithms.Categories.PerformanceBenchmark
{
    public class AlgorithmsToTest
    {
        public void FastAlgorithm()
        {
            Thread.Sleep(TimeSpan.FromMilliseconds(1));
        }
        public void SlowAlgorithm()
        {
            Thread.Sleep(TimeSpan.FromMilliseconds(100));
        }
    }
}