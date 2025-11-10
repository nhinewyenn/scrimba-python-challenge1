# 🛂 Access Control Scanner Challenge
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.

revoked_badge_num = {244, 526, 55, 832, 391}
approved = []
denied = []

while True:
    visitor = input("What's your name?")
    if visitor == "done":
        break

    badge_number = int(input("What's your badge number?"))
    if badge_number in revoked_badge_num:
        denied.append(visitor)
        print("ACCESS DENIED")
        break

    if badge_number not in revoked_badge_num:
        approved.append(visitor)
        print("ACCESS GRANTED")
        break

print("Approved visitor", sorted(approved))
print("Denied visitor", sorted(denied))
print("Number of people who got denied", len(approved))
print("Number of people who got approved", len(denied))
