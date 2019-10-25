# Array

Array occupies a continuous space inside the memory
Array usually be static, size is hard to change

## single dimension

### C#

> int[] x = new int[10];\
> int a = x[4];

## two dimensions

### C#

> int[,] y = new int[2,3];\
> int b = y[0,2];
> int l = y.Length; // l = 2*3 = 6

## Jagged Arrays - array of arrays

### C#

> int[][] y = new int[2][];\
> y[0] = new int[3];\
> int b = y[0][2];
> la = y.Length // 2\
> lb = y[0].Length; // 3\
> lc = y[1].Length; // null reference exception