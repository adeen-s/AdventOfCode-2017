passphrases = []
valid = 0
anagrams = 0
while True:
    passphrase = input()
    if passphrase:
        passphrases.append(passphrase)
    else:
        break
for passphrase in passphrases:
    anagrams = 0
    li = [s for s in passphrase.split()]
    if len(li) != len(set(li)):
        continue
    for s in li:
        for i in range(len(li)):
            if(sorted(s) == sorted(li[i])):
                anagrams += 1
    if anagrams == len(li):
        valid += 1
print(valid)
