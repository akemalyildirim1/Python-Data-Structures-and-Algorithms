"""
We know our inputs will be sorted, which helps us make assertions about where to search for values.

We divide the list in half and compare our target value with the middle element.

If they match, we return the index

If they don’t match, we begin again at the first step with the appropriate half of the original list.

When the list is empty, the target is not found.

O(log n)

"""
#RECURSIVE:

def binary_search(sorted_list, left_pointer, right_pointer, target):
  #4 tane inputu var :
  # ilki düzenlenmiş halde verilen liste, ikincisi listede bakmamız istenen sol index, üçüncüsü listede bakmamız gereken sağ index, dördüncüsü hedef değerimiz
  
  # this condition indicates we've reached an empty "sub-list"
  #sol index, sağ indexe eşit olur veya geçerse o recursive fonksiyona verilen liste boş demektir yani aradığımız değer listede yoktur.
  if left_pointer >= right_pointer:
    return "value not found"
	
  # We calculate the middle index from the pointers now
  #orta değerlerin indexi ve karşılaştırma için değerini buluyoruz.
  mid_idx = (left_pointer + right_pointer) // 2
  mid_val = sorted_list[mid_idx]

  #eğer aradığımız değer mid değeriyse direk indexi döndürebiliyoruz
  if mid_val == target:
    return mid_idx
  
  #eğer aradığımız değer mid değerden küçükse sol tarafa bakmamız gerekiyor bunun için de sol pointer'ı aynı tutarak sağ pointerı mid_idx'e çekmemiz gerekiyor.
  #böylece fonksiyonu tekrar çalıştırdığımızda sadece sol tarafa bakmış olacak ve öbür tarafı önemsememiş olacak
  if mid_val > target:
    # we reduce the sub-list by passing in a new right_pointer
    return binary_search(sorted_list, left_pointer, mid_idx, target)
    
  #eğer aradığımız değer mid değerden büyükse sağ tarafa bakmamız gerekiyor bunun için de  sağ pointer aynı kalırken sol pointer'ı mid+1 indexine çekmemiz gerekiyor böylece mid'i tekrar kontrol etmiyoruz.
  if mid_val < target:
    # we reduce the sub-list by passing in a new left_pointer
    return binary_search(sorted_list, mid_idx + 1, right_pointer, target)
    
    
    
"""
ITERATİVE BINARY SEARCH:
"""

def binary_search(sorted_list, target):
  left_pointer = 0
  right_pointer = len(sorted_list)
  
  # fill in the condition for the while loop
  while left_pointer < right_pointer:
    # calculate the middle index using the two pointers
    mid_idx = (right_pointer+left_pointer)//2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
      return mid_idx
    if target < mid_val:
      # set the right_pointer to the appropriate value
      right_pointer = mid_idx
    if target > mid_val:
      # set the left_pointer to the appropriate value
      left_pointer = mid_idx+1
  
  return "Value not in list"