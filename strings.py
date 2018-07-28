strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''

#for i in words:
    # print(i, end=" ")
#    sentence += i + " "
i = 0
while i < len(strings):
    sentence += strings[i] + " "
    i += 1
    
print(sentence[:-1])

print(' '.join(strings))
