class classreverse:
    def __init__(self, word_S):
        self.s = word_S
    def reverseword(self):
        return self.s[::-1]
word = input("enter string to be reversed")
revobject = classreverse(word)
result = revobject.reverseword()
print("reversed string: ", result)