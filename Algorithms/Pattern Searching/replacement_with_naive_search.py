def pattern_search(text, pattern, replacement, case_sensitive=True):
  #4 inputs:
  # first is the input text
  #second is the pattern
  #third is the string that will added insteead of pattern
  #fourth is the boolean which is about the case sensitivity if it is false then the all strings can be considered as lower
  
  fixed_text = ""
  num_skips = 0
  #indexin replace edilmiş yerler için tekrar eklenmemesi için bunu kullanıyoruz.
  
  for index in range(len(text)):
    
    #burada indexi patternin boyutu kadar ileri alıyoruz ki tekrar texte eklenmesin
    if num_skips > 0:
      num_skips -= 1
      continue

    match_count = 0

    for char in range(len(pattern)): 
      #according to case sensitivity, there are two different conditions
      if case_sensitive and pattern[char] == text[index + char]:
        match_count += 1
      elif not case_sensitive and pattern[char].lower() == text[index + char].lower(): 
        match_count += 1
      else:
        break
    #eğer counter ve pattern boyutu  döngüden sonra eşitse yeni texte ekliyoruz
    if match_count == len(pattern):
      print(pattern, "found at index", index)
      fixed_text += replacement
      num_skips = len(pattern)-1
    #eğer counter sayısı farklıysa textteki karakteri direk yeni texte ekliyoruz
    else:
      fixed_text += text[index]

  return fixed_text