class StringReverser:
    def reverse_words(self, s):
        words = s.split()
        words.reverse()
        return ' '.join(words)
sr = StringReverser()
print(sr.reverse_words('hello .py'))
