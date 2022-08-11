from tools import link_info


@link_info('log.csv')
# Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента:
# строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.
def find_all(target, symbol):
    _list = []

    for i in range(len(target)):
        if target[i] == symbol:
            _list.append(i)
    return _list


@link_info('log.csv')
# Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию
# списка, состоящих из целых чисел, и объединяет их в один отсортированный список.
def merge(list1, list2):
    first, second = list1[:], list2[:]
    result = []
    while first and second:
        if first[0] <= second[0]:
            item = first.pop(0)
        else:
            item = second.pop(0)
        result.append(item)
    result.extend(first if first else second)
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_all('abcdabcaaa', 'a')
    merge([1, 2, 3], [5, 6, 7, 8])
