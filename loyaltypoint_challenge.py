import math

# ☕️ Loyalty Points Engine Challenge
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
# 4. After the loop, call tier_label(total_points)
# 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier

# Purchase history (e.g., 3.75, 7.20, etc.)
purchases = [23.75, 27.20, 25.50, 22.00, 51, 30]
total_pts = 0
total_spent = 0


def earn_points(price):
    return math.floor(price) * 3 #$1 = 3 points

def tier_label(pts):
    if pts < 100:
        return "Bronze"
    if pts >= 500:
        return "Gold"
    else:
        return "Silver"

for pur in purchases:
    total_spent += pur
    total_pts += earn_points(pur)

final_tier = tier_label(total_pts)

print("Total dollar spent", total_spent)
print("Total points earned", total_pts)
print("Final tier", final_tier)
