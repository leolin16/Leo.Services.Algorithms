namespace Leo.Services.Algorithms.Categories.Search.Binary
{
    public static class BinarySearchRecursiveExtension
    {
        public static int BinarySearchRecursive(this int[] array, int value)
        {
            return BinarySearchRecursive(array, 0, array.Length - 1, value);
        }

        private static int BinarySearchRecursive(int[] array, int start,int end, int value)
        {
            if (start > end) return -1;

            int middleElement = (end + start) / 2;

            if(value < array[middleElement])
            {
                return BinarySearchRecursive(array, start, middleElement - 1, value);
            }
            else if(value > array[middleElement])
            {
                return BinarySearchRecursive(array, middleElement + 1, end, value);
            }
            else
            {
                return middleElement;
            }
        }
    }
}