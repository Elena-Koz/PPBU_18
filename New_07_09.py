s = "Здравствуйте, гости!"
# print(s[0])
# print(s[6])
# print(s[-1])
# print(len(s))
# print(s[::1])
# print(s[:12])
# print(s[::-1])
# for i in s:
#     print(i, end=" ")
# print(s[19])
# for i in range(len(s)):
#     print(s[i], end=' ')

# print(s.index(","))
# print(s.isalpha())
# s1 = "12345"
# print(s1.isdigit())
# print(s1.islower())
# print(s1.isupper())
# print(s.startswith('3'))
# print(s.endswith())
#
# print(n := s.lower())
# # print(n)
# # print(s)
# print(n := s.upper())
# print(s.upper())
# print(s.title()) # все слова начинаются с большой буквы
# print(s.capitalize()) # Переменная начинаются с большой буквы
# print(s.rjust(40)) # переменная пишется сразу в 40 знакоместах, выравнивание по правому краю
# print(s.ljust(40)) # переменная пишется сразу в 40 знакоместах, выравнивание по левому краю
# print(s.center(40))
# print(s.strip()) # удаляем пробелы
# print(s.strip("!"))
# print(s.strip("!З ")) # что бы убрать Зб надо убрать пробел перед ней
# print(s.lstrip())
# print(s.rstrip())
# print(s.index(sub:"т", start: 8, end: 11)) #поиск индекса символа или начала подстроки
# print(s.find("т", 8, 11))
# print(s.replace("т", "FT" ))
# print(s.replace("т", "FT" ).replace(".", ""))
# print(s.split())
ls = s.split [] # коллекция структура данных - массив. У коллекций (LS) есть свой тип данных (список)
ls = s.split [", "]
# создает список разделяя слова по пробелу
print(ls)
print(", ".join(ls))
