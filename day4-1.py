passphrases = []
valid = 0
while True:
    passphrase = input()
    if passphrase:
        passphrases.append(passphrase)
    else:
        break
for passphrase in passphrases:
    li = [s for s in passphrase.split()]
    if len(li) == len(set(li)):
        valid += 1
print(valid)
