alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(direction, text, shift):
    if direction.lower() == 'encode':     #decide the shift direction
        var = 1
    elif direction.lower() == 'decode':
        var = -1
    new_text = ''
    for i in range(shift):              #prolong the alphabet list according to the shift
        alphabet.append(alphabet[i])
    for i in text:
        order = alphabet.index(i)
        new_letter = alphabet[order + var*shift]
        new_text += new_letter
    print('Your '+ direction+f'd word is {new_text}')
ceasar(direction,text,shift)
