# word = 'Magnification'
# string = ''
# for i in range (len(word)-1, -1, -1):
#   string += word[i]
#   # print (word[i])
# print (string)


def pillars(num_pill, dist, width):
    return (num_pill-1) * dist * 100 + max(num_pill-2, 0) * width
print (pillars (30, 10, 10))