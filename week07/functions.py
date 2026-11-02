# --- Exercise 1 ---

# Define calculus tax function

def calculate_tax(price, tax_rate):
    return price * tax_rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on 100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on 250 at 8%: ${tax2:.2f}") # 20.00
print(f"Another Tax: ${calculate_tax(150, 0.06):.2f}") # 7.50

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function
price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# --- Exercise 3 ---

# Write it out manually first, then refractor into a function

discounted_price = apply_discount(200, "gold")
tax = calculate_tax(discounted_price, 0.07)
after_tax_price = discounted_price + tax
print(f"After gold discount: ${discounted_price:.2f}") 
print(f"After tax: ${after_tax_price:.2f}")

# Refractor into a function

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted + tax 
    

    print(f"Price before discount: ${price:.2f}")


    # --- Exercise 4 ---
    
    orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

    for price, tier in orders:
        final = final_price(price, tier, 0.07)
        print(f"Order: ${price:.2f}, Tier: {tier}, Final Price: ${final:.2f}")
