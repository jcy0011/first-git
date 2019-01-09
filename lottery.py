from random import randint
def generate_numbers():
    pool = list(range(1, 46))
    lotto = list()
    lotto.append(pool.pop(randint(0, 44)))
    lotto.append(pool.pop(randint(0, 43)))
    lotto.append(pool.pop(randint(0, 42)))
    lotto.append(pool.pop(randint(0, 41)))
    lotto.append(pool.pop(randint(0, 40)))
    lotto.append(pool.pop(randint(0, 39)))
    lotto.sort()
    return lotto
def draw_winning_numbers():
    genlist = generate_numbers()
    gotbonus = None
    while True:
        bonus = randint(1, 45)
        if bonus not in genlist:
            gotbonus = bonus
            break
        else:
            continue
    genlist.append(gotbonus)
    return genlist
def count_matching_numbers(list1, list2):
    count = 0
    for i in range(len(list1)):
        if list1[i] in list2:
            count = count + 1
    return count
def check(numbers, winning_numbers):
    if count_matching_numbers(numbers, winning_numbers[: -1]) == 6:
        return 1000000000
    elif count_matching_numbers(numbers, winning_numbers) == 6:
        return 50000000
    elif count_matching_numbers(numbers, winning_numbers[: -1]) == 5:
        return 1000000
    elif count_matching_numbers(numbers, winning_numbers[: -1]) == 4:
        return 50000
    elif count_matching_numbers(numbers, winning_numbers[: -1]) == 3:
        return 5000
    else:
        return 0

