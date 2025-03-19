def valid_word_abbreviation(word, abbr):
  word_idx, abbr_idx = 0, 0
  while abbr_idx < len(abbr) :
    if abbr[abbr_idx].isdigit():
      if abbr[abbr_idx] == '0':
        return False
      
      num = 0
     
      while abbr_idx < len(abbr) and abbr[abbr_idx].isdigit():
       num = num*10 + int(abbr[abbr_idx])
       abbr_idx += 1
      word_idx += num
    else:
      if word_idx >= len(word) or word[word_idx] != abbr[abbr_idx]:
        return False
      word_idx += 1
      abbr_idx += 1
  return word_idx == len(word) and abbr_idx == len(abbr)

print(valid_word_abbreviation('abhijk', 'a2ijk'))