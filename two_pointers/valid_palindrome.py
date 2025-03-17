def valid_palindrome(s):
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            break
    if left>right:
        return True
    else :
        return False

print(valid_palindrome('a'))