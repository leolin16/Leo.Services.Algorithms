using Arrays;

namespace Leo.Services.Algorithms.Categories.Sort.Bubble
{
    public static class BubbleSortExtension
    {
        public static int[] BubbleSort(this int[] sourceArray)
        {
            // to not modify the source array;
            int[] array = sourceArray.CreateCopy();

            bool swapped = true;
            int lastElement = sourceArray.Length - 1;

            while(swapped)
            {
                swapped = false;
                for(int i = 0; i < lastElement; i++)
                {
                    if(array[i] > array[i + 1])
                    {
                        array.Swap(i, i + 1);
                        swapped = true;
                    }
                }

                lastElement--;
            }

            return array;
        }
    }
}