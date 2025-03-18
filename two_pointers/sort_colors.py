def sort_colors(colors):
  start, current, end = 0, 0, len(colors) - 1
  while current <= end:
    if colors[current] == 0:
      colors[start], colors[current] = colors[current], colors[start]
      start+= 1
      current+= 1
    elif colors[current] == 1:
      current+= 1
    else:
      colors[end], colors[current] = colors[current], colors[end]
      end -=1
      
  return colors

print(sort_colors([1, 1, 0, 2]))
