"""
divide-and-conquer algorithm

Merge sorting takes two steps: splitting the data into “runs” or smaller components, and the re-combining those runs into sorted lists (the “merge”).

When splitting the data, we divide the input to our sort in half. We then recursively call the sort on each of those halves, which cuts the halves into quarters. 
This process continues until all of the lists contain only a single element. Then we begin merging.


Let’s call the two lists left and right. Bothleft and right are already sorted. 
We want to combine them (to merge them) into a larger sorted list, let’s call it both. 
To accomplish this we’ll need to iterate through both with two indices, left_index and right_index.

At first left_index and right_index both point to the start of their respective lists. 
left_index points to the smallest element of left (its first element) and right_index points to the smallest element of right.

Compare the elements at left_index and right_index. 
The smaller of these two elements should be the first element of both 
because it’s the smallest of both! It’s the smallest of the two smallest values.

Let’s say that smallest value was in left. We continue by incrementing left_index to point to the next-smallest value in left. 
Then we compare the 2nd smallest value in left against the smallest value of right. 
Whichever is smaller of these two is now the 2nd smallest value of both.

This process of “look at the two next-smallest elements of each list and add the smaller one to our resulting list” continues on for as long as both lists have elements to compare.
Once one list is exhausted, say every element from left has been added to the result, then we know that all the elements of the other list, right, 
should go at the end of the resulting list (they’re larger than every element we’ve added so far).

Time complexity: Θ(N*log(N))
Space complexity: O(N)
"""

#Merge sortu iki temel fonksiyona ayırarak yazıyoruz
#"merge" fonskiyonu içine verilen iki ayrı listeyi küçükten büyüğe sıralar.
#mergesort fonksiyonu ise recursive bir fonksiyondur

def merge_sort(items):
  #ana fonksiyonumuz budur
  #eğer listenin boyutu 1e eşitse direk o değeri döndürüyor
  if len(items) <= 1:
    return items
  
  #verilen listeyi ikiye bölmek için önce ortadaki indexi buluyoruz
  middle_index = len(items) // 2
  #daha sonra sol ve sağ olarak bu indexe göre ikiye ayırıyouz
  left_split = items[:middle_index]
  right_split = items[middle_index:]
  
  #buradan sonrası recursive!!!
  #sol ve sağ olarak ayırdığımız kısımları merge_sort ile sona kadar ayırıyoruz fakat sonunda merge ettirdiğimiz için elimize listelenmiş şekilde geliyor.
  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)

  return merge(left_sorted, right_sorted)

def merge(left, right):
  #boş bi liste oluşturuyor
  result = []
  
  #hem left hem de right'ın elemanı olduğu sürece while döngüsü içinde hangisinin büyük olduğunu kontrol ediyoruz
  #left ve right için her zaman 0 indexi daha küçük olacağı için listeye önce bunları ekliyoruz ekledikten sonra da pop ile çıkarıyoruz
  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)
   
  #döngü bittiğinde eğer left veya right içinde değer varsa onarı da resulta ekliyoruz
  if left:
    result += left
  if right:
    result += right

  return result