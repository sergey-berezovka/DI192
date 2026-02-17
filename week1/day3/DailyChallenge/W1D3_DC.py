# 1. Letter Index Dictionary
word = input(str("Enter a word: "))

letter_dict = {}

for index, letter in enumerate(word):
    if letter in letter_dict:
        letter_dict[letter].append(index)
    else:
        letter_dict[letter] = [index]

print(letter_dict)

# 2. Affordable Items
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
wallet = int(wallet.replace("$", "").replace(",", ""))

basket = []

for item, price in items_purchase.items():
    clean_price = int(price.replace("$", "").replace(",", ""))

    if wallet >= clean_price:
        basket.append(item)
        wallet -= clean_price

if not basket:
    print("Nothing")
else:
    print(sorted(basket))



