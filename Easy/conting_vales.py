def countingValleys(steps, path):
    sea_level = 0
    level_in_moment = 0
    down = 0
    high = 0
    vale = 0
    for i in path:
        if  i == 'D' :
            if  level_in_moment <= sea_level : down = down + 1
            level_in_moment = level_in_moment - 1

        elif i == 'U':
            if  level_in_moment < sea_level :  high = high + 1
            level_in_moment = level_in_moment + 1
 
        if high == down and level_in_moment == sea_level and high != 0 and down != 0 : 
            vale = vale + 1
            down = 0
            high = 0
            
    return vale

path = input("LISTA: ")
result = countingValleys(len(path), path)
print(result)
