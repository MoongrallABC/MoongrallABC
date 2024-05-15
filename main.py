def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False
    return True

word = input("Gryut: ").lower()
if is_palindrome(word):
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")