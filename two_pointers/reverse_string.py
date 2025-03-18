def reverse_words(sentence):
  sentence = sentence.strip()
  sentence = sentence.split()
  print(sentence)
  left = 0
  right = len(sentence) - 1
  while left <= right:
    sentence[left], sentence[right] = sentence[right], sentence[left]
    left += 1
    right -= 1
  return ' '.join(sentence)

  
print(reverse_words('hello world '))