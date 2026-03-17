#Challenge: Palindrome Checker
print ("Welcome to the Palindrome Checker!")
word = input("Please enter a word: ").lower()
if word == word[::-1]:
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")
