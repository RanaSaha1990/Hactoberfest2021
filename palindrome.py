word = input("Enter a word to check is it Palindrome?\n")
word = word.lower()
print("Your entered word is")
j = 0
for letter in word:  # for collecting the letters
    i = letter
    i = i.upper()
    j = j + 1
    print(i, " ", end="")
n = j
print("\nNumber of letters in the given word is", n)
k = 0
while k < n:  # for matching the letters
    if word[k] != word[(n - 1) - k]:
        print("The word is not a Palindrome")
        break
    k = k + 1
if k == n:
    print("The word is a Palindrome")
