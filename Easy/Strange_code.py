def strangeCounter(t):
    inicial_value = 3
    value         = inicial_value
    t_now         = 1
    while(t_now < t):
        if value == 1:
            value         = (2 * inicial_value)
            inicial_value = value
        else: value = value - 1
        t_now = t_now  + 1

    return value

def strangeCounter_1(t):
    inicial_value = 3
    flag = 0
    while( flag != 1):
        t_inic = inicial_value - 2
        t_fim  = t_inic + inicial_value - 1
        if t_inic <= t and t <= t_fim : flag = 1
        else : inicial_value = 2 * inicial_value

    if   t_inic == t : return inicial_value
    elif t_fim  == t : return 1

    t_inic = inicial_value - 2
    value = inicial_value
    while(t_inic < t):
        t_inic = t_inic + 1
        value = value - 1

    return value

def strangeCounter_2(t):
    inicial_value = 3
    flag = 0
    while( flag != 1):
        t_inic = inicial_value - 2
        t_fim  = t_inic + inicial_value - 1
        value = inicial_value
        if t_inic <= t and t <= t_fim :
            value = value - (t - t_inic )
            flag = 1
        else : inicial_value = 2 * inicial_value

    if   t_inic == t : return inicial_value
    elif t_fim  == t : return 1

    return value

t = int(input())
result = strangeCounter(t)
print(result)
result = strangeCounter_1(t)
print(result)
result = strangeCounter_2(t)
print(result)
