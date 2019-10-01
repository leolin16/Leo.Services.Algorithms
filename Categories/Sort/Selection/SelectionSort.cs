using Arrays;

namespace Leo.Services.Algorithms.Categories.Sort.Selection
{
    public static class SelectionSortExtension
    {
        public static int[] SelectionSort(this int[] sourceArray)
        {
            // to not modify the source array;
            int[] array = sourceArray.CreateCopy();

            for(int i = 0; i < array.Length; i++)
            {
                int min = i;
                for(int j = i + 1; j < array.Length; j++)
                {
                    if (array[j] < array[min]) min = j;
                }

                if (min == i) continue;

                array.Swap(i, min);
            }

            return array;
        }
    }
}