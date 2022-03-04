def pattern_search(text, pattern):
  """
  The algorithm begins by iterating through the text and setting a variable match_count equal to 0.

  Then, for each index of the text, the algorithm iterates through the pattern to check for matching characters, 
  and if found, increments match_count. Otherwise, the search breaks the pattern iteration and moves onto the next index in text.

  Each time the pattern iteration is completed, the match_count is compared to the length of the pattern to determine if a match is found.
  """
  #Input textini ve bulunması gereken patterni veriyoruz önce bunu bastırıyor.
  #fonksiyon koda verilen textteki bütün karakterleri inceliyor.
  print("Input Text:", text, "Input Pattern:", pattern)
  for index in range(len(text)):
    #bütün karakterlere bakmak için bir index tanımlıyoruz
    print("Text Index:", index)
    match_count = 0
    #match_count eşleşen karakter sayısını sayıyor
    #eğer alttaki döngü içinde match_count pattern lenghthine eşit olursa başarıyla bulmuş oluyor
    for char in range(len(pattern)):
    #bu döngü de patternin indexlerini sayıyor
    #eğer patternin ilk karakteri textte bulunduğumuz karakterle eşleşmezse direk tekstteki öbür karaktere geçiş yapılıyor
    #eğer eşleşir ise text de patternin indexi ile aynı oranda artırılarak kontrolü sağlanıyor eğer counter ve length aynı olursa içinde bulmuş oluyoruz.
      print("Pattern Index:", char)
      if pattern[char] == text[index + char]:
        #eşleşme olduğunda counterı artırıyor
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)

