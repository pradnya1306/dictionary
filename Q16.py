word_freq = {
    'Hello' : 56,
    'At'    : 23,
    'Test'  : 43,
    'Why'   : 11,
    'This'  : 78,
}
# Iterate over a dictionary sorted by key in ascending order
for key in sorted(word_freq):
    print(key, ' :: ', word_freq[key])


word_freq = {
    'Hello' : 56,
    'At'    : 23,
    'Test'  : 43,
    'Why'   : 11,
    'This'  : 78,
}
# Iterate over a dictionary sorted by key in descending order
for key in sorted(word_freq, reverse=True):
    print(key, ' :: ', word_freq[key])

word_freq = {
    'Hello' : 56,
    'At'    : 23,
    'Test'  : 43,
    'Why'   : 11,
    'This'  : 78,
}
# Iterate over a dictionary sorted by values
for key, value in sorted(word_freq.items(),
                        key=lambda item: item[1]):
    print(key, ' :: ', value)

word_freq = {
    'Hello' : 56,
    'At'    : 23,
    'Test'  : 43,
    'Why'   : 11,
    'This'  : 78,
}
# Iterate over key-value pairs of dictionary
# sorted by values
for key, value in sorted(   word_freq.items(), 
                            key=lambda item: item[1],
                            reverse=True):
    print(key, ' :: ', value)


sorted_dict = dict( sorted(word_dict.items(),
                           key=lambda item: item[1],
                           reverse=True))
print('Sorted Dictionary: ')
print(sorted_dict)