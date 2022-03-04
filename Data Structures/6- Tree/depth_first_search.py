"""
Recursive bir algoritma:
Örneğin :
A
├─B
   ├─D
   └─E
└─C
   ├─F
   └─G
   
şeklinde bi ağacımız olsun ve D yi bulmaya çalışalım
başta A ile başlayacak kod path=(A) olacak
for döngüsüne geldiğinde path_found=dfs(B,D,(A)) şeklinde çalışacak
B deki recursive içinde path (A,B) şeklini alacak
D için olduğunda da (A,B,D) şeklinde gelip return olmaya başlayacak ve o pathi return etmiş olacak
"""

def dfs(root, target, path=()):
  #path bir tuple olarak veriliyor.
  path = path + (root,)

  if root.value == target:
    return path

  for child in root.children:
    path_found = dfs(child, target, path)

    if path_found is not None:
      return path_found

  return None