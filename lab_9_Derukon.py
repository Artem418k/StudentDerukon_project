#Завдання 1

def mysplit(string):
    string = string.strip() + ' '

    list_split = []

    if string.isspace() or string == "":
        return list_split

    if string.find(' ') == -1:
        list_split.append(string)
        return list_split

    start = 0
    end = string.find(' ')

    while end != -1:
        list_split.append(string[start:end])
        start = end + 1
        end = string.find(' ', start)

    return list_split


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

#Завдання 2

def display_digit(digit):
    segments = [
        ['###', '# #', '# #', '# #', '###'],  # 0
        ['  #', '  #', '  #', '  #', '  #'],  # 1
        ['###', '  #', '###', '#  ', '###'],  # 2
        ['###', '  #', '###', '  #', '###'],  # 3
        ['# #', '# #', '###', '  #', '  #'],  # 4
        ['###', '#  ', '###', '  #', '###'],  # 5
        ['###', '#  ', '###', '# #', '###'],  # 6
        ['###', '  #', '  #', '  #', '  #'],  # 7
        ['###', '# #', '###', '# #', '###'],  # 8
        ['###', '# #', '###', '  #', '###']   # 9
    ]

    if digit < 0:
        print("Введіть невід'ємне ціле число.")
        return

    digits = list(str(digit))
    for line in range(5):
        for d in digits:
            d = int(d)
            print(segments[d][line], end=' ')
        print()


number = int(input("Введіть невід'ємне ціле число: "))
display_digit(number)

#Завдання 3
def caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    return encrypted_message


message = input("Введіть повідомлення: ")
shift = int(input("Введіть значення зсуву: "))

encrypted_message = caesar_cipher(message, shift)
print("Зашифроване повідомлення:", encrypted_message)

#Приклад 4

def caesar_decipher(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_message += shifted_char
        else:
            decrypted_message += char
    return decrypted_message


encrypted_message = input("Введіть зашифроване повідомлення: ")
shift = int(input("Введіть значення зсуву: "))

decrypted_message = caesar_decipher(encrypted_message, shift)
print("Дешифроване повідомлення:", decrypted_message)

#Завдання 1
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                start = ord('a')
                end = ord('z')
            else:
                start = ord('A')
                end = ord('Z')
            shifted_char = chr((ord(char) - start + shift) % (end - start + 1) + start)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text


text = input("Введіть рядок для шифрування: ")
shift = int(input("Введіть значення зсуву (1-25): "))

if shift < 1 or shift > 25:
    print("Некоректне значення зсуву. Введіть число від 1 до 25.")
else:
    encrypted_text = caesar_cipher(text, shift)
    print("Закодований текст:", encrypted_text)


