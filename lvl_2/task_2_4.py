# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    pass
    rem=s.replace('!','')
    return rem
print("Пункт А")
s=input("Введите сторку:")
print("Пункт А")
print(f'начальная строка {s} , строка после удаления всех восклицательных знаков {remove_exclamation_marks(s)}')
# Пункт B.
# Удалите восклицательный знак из конца строки.
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    
    if s[-1] == '!':
        temp_s = ""
        for i in range(0, len(s)):
            if i == len(s)-1: 
                break
            else:
                temp_s+=s[i]
        s = temp_s
    return s
    # if s[-1]
    # for i in range(0,len(s)):
    #     if s[i]
    # i=0
    # while i < 3 and s[-1]=="!":
    #     s=s[:-1]
    #     i+=1
    # return(s)
e=remove_last_em(s)
print("Пункт Б")
print(f'начальная строка {s} , строка после удаления одного восклицательного знака из конца строки {e}')


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    pass