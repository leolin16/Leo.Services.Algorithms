using System;
using BenchmarkDotNet.Attributes;

namespace Leo.Services.Algorithms.Categories.PerformanceBenchmark
{
    public class AdvancedMeasurement
    {
        AlgorithmsToTest _test = new AlgorithmsToTest();

        [Benchmark]
        public void TestFastAlgorithm() => _test.FastAlgorithm();
        [Benchmark]
        public void TestSlowAlgorithm() => _test.SlowAlgorithm();
    }
}