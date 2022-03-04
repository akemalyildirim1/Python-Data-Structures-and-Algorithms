"""
Quicksort uses a divide and conquer strategy,

We choose a single pivot element from the list. Every other element is compared with the pivot, which partitions the array into three groups.
    1- A sub-array of elements smaller than the pivot.
    2- The pivot itself.
    3- A sub-array of elements greater than the pivot.

The process is repeated on the sub-arrays until they contain zero or one element. 
Elements in the “smaller than” group are never compared with elements in the “greater than” group. 
If the smaller and greater groupings are roughly equal, this cuts the problem in half with each partition step!

"""
"""
We established a base case where the algorithm will complete when the start and end pointers indicate a list with one or zero elements

If we haven’t hit the base case, we randomly selected an element as the pivot and swapped it to the end of the list

We then iterate through that list and track all the “lesser than” elements by swapping them with the iteration index and incrementing a lesser_than_pointer.

Once we’ve iterated through the list, we swap the pivot element with the element located at lesser_than_pointer.

With the list partitioned into two sub-lists, we repeat the process on both halves until base cases are met.

"""

from random import randrange, shuffle

def quicksort(list, start, end):
  # this portion of list has been sorted
  #start indexi endden büyük olursa duruyor bu recursive için base case!
  if start >= end:
    return
  print("Running quicksort on {0}".format(list[start: end + 1]))
  #fonksiyonun hızlılığını düşürmemek için random şekilde pivot seçiyoruz
  # select random element to be pivot
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  print("Selected pivot {0}".format(pivot_element))
  # swap random element with last element in sub-lists
  #önce o pivotu listenin sonuna getiriyoruz
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # tracks all elements which should be to left (lesser than) pivot
  #less_than_pointer'ı takip etmek için önce starta eşitliyoruz start bizim göreceli 0ımız
  less_than_pointer = start
  
  for i in range(start, end):
    #bütün elemanlar için dönmemiz gerekiyor
    # we found an element out of place
    if list[i] < pivot_element:
      #eğer pivot eleman listedeki elemandan daha büyükse less than pointerdaki elemanla bunu değiştiriyoruz
      # swap element to the right-most portion of lesser elements
      print("Swapping {0} with {1}".format(list[i], pivot_element))
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      # tally that we have one more lesser element
      less_than_pointer += 1
  # move pivot element to the right-most portion of lesser elements
  #en sonda pivot elemanla less_than pointer indexini değiştiriyoruz böylece sağ ve sol diye ikiye ayırmış olduğumuz bir liste elimizwe geliyor
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  print("{0} successfully partitioned".format(list[start: end + 1]))
  # recursively sort left and right sub-lists
  #sol ve sağ listeler için tekrar recursive şekilde çağırıyoruz
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)