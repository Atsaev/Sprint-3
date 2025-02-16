class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    # def cipher(self, original_text, shift):
    #     # Метод должен возвращать зашифрованный текст
    #     # с учетом переданного смещения shift.
    #     result = []
    #     for letter in original_text.lower():
    #         if letter in self.alphabet:
    #             index = self.alphabet.index(letter)
    #             index = (index + shift) % len(self.alphabet)
    #             # добавляем зашифрованный символ
    #             result.append(self.alphabet[index])
    #         else:
    #             result.append(letter)  # добавляем символ без изменений
    #     return ''.join(result)

    # def decipher(self, cipher_text, shift):
    #     # Метод должен возвращать исходный текст
    #     # с учётом переданного смещения shift.
    #     result = []
    #     for letter in cipher_text.lower():
    #         if letter in self.alphabet:
    #             index = self.alphabet.index(letter)
    #             index = (index - shift) % len(self.alphabet)
    #             result.append(self.alphabet[index])
    #         else:
    #             result.append(letter)
    #     return ''.join(result)
    def process_text(self, text, shift, is_encrypt):
        result = []
        for letter in text.lower():
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                if is_encrypt:
                    index = (index + shift) % len(self.alphabet)
                else:
                    index = (index - shift) % len(self.alphabet)
                result.append(self.alphabet[index])
            else:
                result.append(letter)
        return ''.join(result)

# cipher_master = CipherMaster()
# print(cipher_master.cipher(
#     original_text='Однажды ревьюер принял проект с первого раза, ' +
#     'с тех пор я его боюсь',
#     shift=2
# ))
# print(cipher_master.decipher(
#     cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
#     shift=-3
# ))


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
