using System;

namespace CsharpIntro
{
    // public class IntPair
    // {
    //     public int First { get; }
    //     public int Second { get; }
    //     public IntPair(int first, int second)
    //     {
    //         First = first;
    //         Second = second;
    //     }
    // }
    public class Pair<T>
    {
        public T First { get; }
        public T Second { get; }
        public Pair(T first, T second)
        {
            First = first;
            Second = second;
        }
    }
}