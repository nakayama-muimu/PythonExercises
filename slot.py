from random import randrange


credits = 100
m = 0

while credits > 0:
    m = max(m, credits)
    # Decide betting amount
    bet = 10
    while credits > bet * 10:
        bet *= 10
    s = set()
    v = []
    for i in range(0, 3):
        a = str(randrange(1,8))
        s.add(a)
        v.append(a)
    l = len(s)
    if l == 3:
        d = -bet
    if l == 2:
        d = bet
    if l == 1:
        if v[0] == '7':
            d = bet * 50
        else:
            d = bet * 10
    print(f"{credits = }, {bet = }, [{v[0]}{v[1]}{v[2]}] gain/loss = {d}")
    credits += d

print(f"max credits = {m}")