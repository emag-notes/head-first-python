vowels = ["a", "e", "i", "o", "u"]
word = input("単語を入力してください。母音を探します。")
found = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, "の出現回数は", v, "回")
