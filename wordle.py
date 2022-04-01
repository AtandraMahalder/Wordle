# Program written by Atandra Mahalder
# 04/01/2022

# words to extract position and occurance of letters:
# brick
# glent
# jumpy
# vozhd
# waqfs
# x is missing and it's occurence can be deduced from occurance of rest 25 letters

print('Enter number of lines of information:')
n = int(input())

pos_char = {}
chars = set()

print('Enter information about letters:')
for _ in range(n):
    sc = input().split()
    if len(sc) == 2:
        pos_char[sc[1]] = sc[0]
    chars.add(sc[0])

words = []
def generate(i, temp):
    if i == 5:
        if len(set(temp)) == len(chars):
            words.append(''.join(temp))
        return

    if str((i + 1)) in pos_char.keys():
        temp[i] = pos_char[str((i + 1))]
        generate(i + 1, temp)
        return
    
    for c in chars:
        temp[i] = c
        generate(i + 1, temp)

generate(0, [None]*5)

dict_words = set()
with open('valid_words.txt') as file:
    for line in file:
            dict_words.add(line[:-1])

for word in words:
    if word in dict_words:
        print(f'{word} is a possible answer')