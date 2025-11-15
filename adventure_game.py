"""Dot Point Summary: Adventure Game Description
Game Concept:

Your village is under attack by a Germanic tribe
You must visit stores and collect the right items to save the village (and impress someone special)
All prices are in gold pieces (excluding VAT!)

Key Features:
Three Stores Available:
Freelancing Shop (hire characters like Brian, Black Knight, Biccus Diccus, Grim Reaper, Minstrel)
Antique Shop (buy items like French Castle, Wooden Grail, Scythe, Catapult, German Joke)
Pet Shop (purchase Blue Parrot, White Rabbit, or Newt)


Shopping Mechanics:
You can buy one item from each store
Items are removed from store inventory once purchased
Type the item name (like 'newt') to buy it
Type 'exit' to leave a store without buying anything


Money System:
You start with 1,000 gold pieces in your purse
The game tracks total cost and remaining gold
At the end, it shows what you bought and your spending summary


Special Features:
The game prints all store inventories before and after shopping (as if a big corporation bought all the stores)
There's a secret way to actually make money while solving the problem (hint: look at the prices carefully!)
The code needs completion - you'll need to fill in the loop structure to make it work



Hidden Easter Egg: Some items have negative prices (like the minstrel at -15 gold), meaning they actually pay you to take them!
"""

#create stores
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}
all_items = {**freelancers, **antiques, **pet_shop}
del all_items["name"]
print(all_items)

cart = {}
count = 0
starting_money = 1000

for v in freelancers, antiques, pet_shop:
    ask_buyer = input(f"Welcome to shop {v['name']}! Which item do you want to buy? (type exit to buy nothing)").lower()

    if ask_buyer in v and ask_buyer != "name":
        purchased_items = v.pop(ask_buyer)
        count += purchased_items
        cart.update({ask_buyer: purchased_items})
        all_items.pop(ask_buyer)
    elif ask_buyer == "exit":
        continue
    else:
        print("Item does not exist from the store")

balance = starting_money - count
print("Total Balance", balance)
print("Purchased item from player", cart)
print("Current shop item", all_items)