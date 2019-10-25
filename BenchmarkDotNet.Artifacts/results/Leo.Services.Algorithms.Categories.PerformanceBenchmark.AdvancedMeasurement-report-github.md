``` ini

BenchmarkDotNet=v0.11.5, OS=Windows 10.0.18362
Intel Core i7-6770HQ CPU 2.60GHz (Skylake), 1 CPU, 8 logical and 4 physical cores
.NET Core SDK=2.1.802
  [Host]     : .NET Core 2.1.13 (CoreCLR 4.6.28008.01, CoreFX 4.6.28008.01), 64bit RyuJIT
  DefaultJob : .NET Core 2.1.13 (CoreCLR 4.6.28008.01, CoreFX 4.6.28008.01), 64bit RyuJIT


```
|            Method |       Mean |     Error |    StdDev |
|------------------ |-----------:|----------:|----------:|
| TestFastAlgorithm |   1.955 ms | 0.0108 ms | 0.0084 ms |
| TestSlowAlgorithm | 100.815 ms | 0.1583 ms | 0.1481 ms |
