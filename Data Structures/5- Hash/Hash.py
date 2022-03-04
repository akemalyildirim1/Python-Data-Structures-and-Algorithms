class HashMap:
  def __init__(self, array_size):
    #öncelikle arrayin limitlerini belirliyoruz. Bu bizim modulus değerimiz olacak.
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    #hash fonksiyonu bize hash değerini verecek ayrıca linear probingi kullanacağımız zaman ikinci bir parametre olan count_collisions ı da vererek bunu sağlıyoruz.
    #bu fonksiyon hashcodu döndürüyor indexi bulmak için compressoru kullanmamız lazım
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    #hashten gelen değerin indexini bulmak için kullanıyoruz
    return hash_code % self.array_size

  def assign(self, key, value):
    #hashe eleman eklmek içn kullanılıyor
    #gerekli index compressor fonksiyonunu hashten gelen değerde kullandığımızda bulunuyor.
    array_index = self.compressor(self.hash(key))
    #önce bu indexteki değeri alıp bir değişkene atıyoruz
    current_array_value = self.array[array_index]
    
    #eğer bu indexteki değer hiç yoksa direk verilen değeri buraya atıyoruz.
    if current_array_value is None:
      self.array[array_index] = [key, value]
      return
    
    #eğer indexte değer var ise bunun bizim keyimiz ile eşleşip eşleşmediğini bulmamız gerekiyor eğer eşleşmiyorsa linear probingi kullanarak sonraki değerlere geçiş yapıyoruz.
    #eşleşiyorsa keyin değerini yeniliyoruz.
    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # Collision!
    
    #fonksiyon buraya kadar geldiğine göre indexte bir değer var ve bu değer bizim keyimiz ile eşleşmiyor bu nedenle linear probing yaparak sonraki indexleri kontrol etmemiz gerekiyor.
    number_collisions = 1

    while(current_array_value[0] != key):
      #döngü keyi bulana kadar dönecek 
      #collision number ekleyip yeni bir array indexi elde ediyoruz ve bunu da current_array_value'ya atıyoruz.
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]
       
      #yeni aldığımız index boş ise direk buraya atıyoruz.
      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return
      
      #yeni index dolu ise ve key ile eşleşiyorsa eski keyin değeirni güncelliyoruz.
      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return
       
      #yeni index dolu ve key eşleşmiyorsa, sonraki indexleredevam ediyoruz.
      number_collisions += 1

    return

  def retrieve(self, key):
    #hashten istediğimiz keyin değerini bulmak için bu fonksiyonu kullanıyoruz.
    #önce compressorun içine hash fonksiynu vererek keyimizin indexini buluyoruz.
    array_index = self.compressor(self.hash(key))
    #muhtemel olan değerimiz için bulduğumuz indexteki değeri bir değişkene atıyoruz.
    possible_return_value = self.array[array_index]

    #eğer bu değişken boş ise alabileceğimiz bir değer yoktur.
    if possible_return_value is None:
      return None

    #eğer bu değişken var ise ve keyimiz eşleşiyorsa direk istediğimiz değeri çakışma olmadan bulmuşuz demektir
    if possible_return_value[0] == key:
      return possible_return_value[1]

    #eğer bu değişken var ise ve keyimiz eşleşmiyorsa çakışma durumuna giriyor ve linear probingi kullanmaya başlıyoruz bunun için çakışma katsayısını önce 1e eşitliyoruz
    retrieval_collisions = 1

    while (possible_return_value[0] != key):
      #döngü keyi bulana kadar devam ediyor
      #önce yeni bir index bulmamız gerekiyor yani sonraki index
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      #yeni bulduğumuz index boş ise aradığımız değer bu hash mapte yoktur
      if possible_return_value is None:
        return None
      
      #eğer sonraki indexte bulursak bunu döndürüyoruz
      if possible_return_value[0] == key:
        return possible_return_value[1]

      #eğer index var ise ve key eşleşmiyorsa sonraki indexleri kontrol etmeye devam ediyoruz
      retrieval_collisions += 1

    return