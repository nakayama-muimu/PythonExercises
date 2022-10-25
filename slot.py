credits = 100

while credits > 0:
    print(f"${credits = }")
    # Decide betting amount
    bet = 10
    while credits > bet * 10:
        bet *= 10
    print(f"${bet = }")
    