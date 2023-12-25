# ✔Функция получает на вход строку из двух чисел через пробел. ✔
# Сформируйте словарь, где ключом будет символ из Unicode, а значением
# —  целое число. ✔Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def solution(nums: str):
    nums = list(map(int, nums.split()))
    my_dict = {}
    for num in range(min(nums), max(nums) + 1):
        my_dict[chr(num)] = num
    return my_dict


print(solution('678 690'))