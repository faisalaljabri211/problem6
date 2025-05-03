def count_fruits_on_house(s, t, a, b, apples, oranges):
    apple_positions = [a + d for d in apples]
    orange_positions = [b + d for d in oranges]

    apples_on_house = sum(s <= pos <= t for pos in apple_positions)
    oranges_on_house = sum(s <= pos <= t for pos in orange_positions)

    print(apples_on_house)
    print(oranges_on_house)

s, t = 7, 10
a, b = 4, 12
apples = [2, 3, -4]
oranges = [3, -2, -4]
count_fruits_on_house(s, t, a, b, apples, oranges)

s, t = 7, 10
a, b = 5, 15
apples = [-2, 2, 1]
oranges = [5, -6]
count_fruits_on_house(s, t, a, b, apples, oranges)
