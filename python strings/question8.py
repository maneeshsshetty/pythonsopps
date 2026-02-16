def longest_word_length(words):
    if not words:
        return 0
 
    return max(len(word) for word in words)


def longest_word_length_v2(words):
    if not words:
        return 0
    
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

words1 = ['python', 'is', 'awesome']
print(f"Words: {words1}")
print(f"Longest word length: {longest_word_length(words1)}")
print()

words2 = ['a', 'bb', 'ccc', 'dddd']
print(f"Words: {words2}")
print(f"Longest word length: {longest_word_length(words2)}")
print()

words3 = ['programming']
print(f"Words: {words3}")
print(f"Longest word length: {longest_word_length(words3)}")
print()

words4 = []
print(f"Words: {words4}")
print(f"Longest word length: {longest_word_length(words4)}")
print()

print("=== Method 2: Using loop ===")
words5 = ['hello', 'world', 'python', 'code']
print(f"Words: {words5}")
print(f"Longest word length: {longest_word_length_v2(words5)}") 