""" "
Given k lists of soted integers

write a function that finds the smallest range that encompasses at least one number from each of the k lists.

list 1: [5,7,13,17]
list2 : [2,4,8,16]
list3 : [10,20,30]

"""



def smallest_range(
    list_1: list[int], list_2: list[int], list_3: list[int]
) -> list[int]:
    


if __name__ == "__main__":
    list_1 = [5, 7, 13, 17]
    list_2 = [2, 4, 8, 16]
    list_3 = [10, 20, 30]

    print(f"Encompas: {smallest_range(list_1, list_2, list_3)}")
