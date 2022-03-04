"""
Bubble sort is an introductory sorting algorithm that iterates through a list and compares pairings of adjacent elements.

We implement the algorithm with two loops.

The first loop iterates as long as the list is unsorted and we assume it’s unsorted to start.

Within this loop, another iteration moves through the list. For each pairing, the algorithm asks:

In comparison, is the first element larger than the second element?

If it is, we swap the position of the elements. The larger element is now at a greater index than the smaller element.

When a swap is made, we know the list is still unsorted. The outer loop will run again when the inner loop concludes.

The process repeats until the largest element makes its way to the last index of the list. The outer loop runs until no swaps are made within the inner loop.

O(n^2)
"""

#we need helper function which is called "swap" to change the position of the elements in the list.
def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp

#optimize edilmemiş halde bu şekilde
def bubble_sort_unoptimized(arr):
  for el in arr:
    for index in range(len(arr) - 1):
      if arr[index] > arr[index + 1]:
        swap(arr, index, index + 1)
        
#optimize edilmiş ve kullanılması gereken hali:

def bubble_sort(arr):
  #içerideki her döngünün sonunda listenin en sağındaki elemanlar düzenlenmiş oluyor
  #bunun için len(arr)-i-1 yaptık yani ikinci döngüde artık en sağdaki iki elemanı kontrol etmeyecek
  for i in range(len(arr)):
    # iterate through unplaced elements
    for idx in range(len(arr) - i - 1):
      if arr[idx] > arr[idx + 1]:
        # replacement for swap function
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

