# sort

## Selection Sort

* Devide array into sorted and unsorted part
* Find smallest number in unsorted part
* Swap it with first number in unsorted part
* Add the first number from unsorted part to the end of sorted part
* Repeat until there is only one element in unsorted part

Complexcity: $\frac{1}{2} N^2$ -> O($N^2$)

## Bubble sort

* swap when left item is bigger than the right
* big values are bubbling up the array
* when we went through the array without any swaps, the array is considered sorted

Complexcity: O($N^2$)

## Merge Sort

* split array into halves recursively until we have single elements(O(logN)) -> merge them together(O(N))
* need additional O(N) memory to be able to merge in O(N) time
* compare from splitted elements and merge along, at each step, individual element group is sorted already, comparing happens from left to right, pick the smaller one and put it to the left of the next step.

Complexcity: O($Nlog(N)$)