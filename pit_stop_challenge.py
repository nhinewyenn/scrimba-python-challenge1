# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

total_race_time = input("Total race time in second?")
how_many_stops = input("How many stops were made?")
avg_pit_stop = input("average pit stop per second?") 
total_pit_stop = float(how_many_stops) * float(avg_pit_stop)
percentage_spent_in_pit = (total_pit_stop/float(total_race_time)) * 100


print(total_race_time, how_many_stops, avg_pit_stop, total_pit_stop, percentage_spent_in_pit)

if percentage_spent_in_pit > 5:
    print("You need a new pit crew")