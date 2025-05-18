word = input()

A = ''
for i in range(len(word) - 1):
    if (word[i] != word[i + 1]):
        A += word[i]
A += word[len(word) - 1]

print(A)