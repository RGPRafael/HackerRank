
def howManyGames1(p, d, m, s):
    # Return the number of games you can buy
    games = 0
    start_price = p
    budget = 0
    minimum = m
    while(budget + start_price <= s):
        budget = budget + start_price
        if start_price - d > minimum : start_price = start_price - d
        else :                         start_price = minimum
        games += 1
    return games

pdms = input().split()
p = int(pdms[0])
d = int(pdms[1])
m = int(pdms[2])
s = int(pdms[3])
answer = howManyGames(p, d, m, s)
print(answer)
answer = howManyGames1(p, d, m, s)
print(answer)
