# Создайте программу, которая фильтрует список строк и возвращает список, содержащий только
# имена ваших друзей.
#
# Если в имени ровно 4 буквы, можете быть уверены, что это ваш друг! В противном случае,
# вы можете быть уверены, что он не...
#
# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]

def friend(x):
    friend_list = []
    for friend in x:
        if len(friend) == 4:
            friend_list.append(friend)
    return friend_list

x = ['Толя', 'Оля', 'Петя', 'Вася', 'Сергей','Витя']
print(friend(x))


