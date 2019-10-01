using System;

namespace CsharpIntro
{
    public class Rectangle
    {
        public int SideA { get; }
        public int SideB { get; }
        public Rectangle(int sideA, int sideB)
        {
            SideA = sideA;
            SideB = sideB;
        }
        public long GetArea()
        {
            return SideA * SideB;
        }
        public static int GetNumberOfAngles() => 4;
    }
}