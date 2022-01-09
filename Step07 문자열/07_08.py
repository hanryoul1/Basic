alphabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for unit in alphabet_list:  # 'ABC'
    for i in unit:  # 'ABC' -> 'A', 'B', 'C'
        for x in word:
            if i == x: 
                time += alphabet_list.index(unit) + 3  #  'ABC' == 3초(0 + 3) 

print(time)