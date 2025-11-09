# You sell lemonade over 2 weeks, list shows the number of lemonade sold/week
# Add another day to week 2 list by capturing a number as input
# price 1.5$
# combine 2 lists into a list called sale
# Calculate + print how much you have earned (worst day, best day, separately, total)
# Hint: 3 prints in total

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

extra_day = int(input(("Extra sales for week 2")))
sales_w2.append(extra_day)
sales.extend(sales_w1)
sales.extend(sales_w2)

worst_profit = min(sales) * 1.5
best_profit = max(sales) * 1.5
wk1_total = sum(sales_w1) * 1.5
wk2_total = sum(sales_w2) * 1.5

print(f"Worst day: {worst_profit}, best day {best_profit}")
print(f"Week 1 total {wk1_total}, week 2 total {wk2_total}")
print("total", sum(sales) * 1.5)
