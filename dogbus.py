# 🐾 Dog Bus Tracker — Challenge Steps
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time
#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
#
# 3. Add one new pet if there’s room on the bus.
#    - Use MAX_SEATS to limit capacity.
#    - Dynamically assign the next seat number.
#    - Print the updated roster showing all pets after pickup.
#
# 4. Ask which pet leaves early.
#    - Remove that pet from the bus.
#    - Print a message saying they’ve headed home.
#
# 5. Print a final roster listing the remaining pets and their dropoff times.

MAX_SEATS = 5
bus = {
  1: {
    "name": "Max",
    "breed": "Golden Retriever",
    "pickup time": 8.30,
    "dropoff time": 14.00,
  },
  2: {
    "name": "Bella",
    "breed": "French Bulldog",
    "pickup time": 8.30,
    "dropoff time": 16.30,
  },
  3: {
    "name": "Charlie",
    "breed": "Labrador",
    "pickup time": 9.00,
    "dropoff time": 18.00
  },
}

for key, value in bus.items():
    print(f"{key} - name: {value["name"]}, breed: {value["breed"]}, pickup time: {value["pickup time"]}")

if len(bus) < MAX_SEATS:
    name = input("Your pet name?").capitalize()
    breed = input("Breed?").capitalize()
    pickup = float(input("Pickup time (number only)?"))
    dropoff = float(input("Dropoff time (number only?"))
    next_seat = max(bus.keys()) + 1

    bus[next_seat] = {
    "name": name, 
    "breed": breed,
    "pickup time": pickup,
    "dropoff time": dropoff,
    } 
print(bus)

leave_early = input("Which pet leave early (name)?").capitalize()

for key, value in bus.items():
    if value["name"] == leave_early:
        pet_leave = key
        print(f"{pet_leave} - {value["name"]} has gone")
    else:
        print(f"{leave_early} does not exist")

bus.pop(pet_leave)
print(bus)