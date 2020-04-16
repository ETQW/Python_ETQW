'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.'''

out_f = open("test2.txt", "w")
str_list = ['fsdf fsdf\n', 'sfsdf sfsdfs sf\n', 'f dh gdf ssdd\n']
out_f.writelines(str_list)
out_f.close()
out_f = open("test2.txt", "r")
i = 0
for s in out_f:
    i += 1
    s = s.split()
    l = len(s)
    print(f'В строке {s} файла {l} слова')
print(f'В файле всего строк: {i}')
