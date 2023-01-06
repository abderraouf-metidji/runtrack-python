def chiffrement(lettre, decalage):

    num = ord(lettre) + decalage
    if num > 122:
        num -= 26

    return chr(num)

def cesar(message, decalage):
    chiffré = ""
    for lettre in message:
        if lettre == " ":
            chiffré += " "

        else: chiffré += chiffrement(lettre, decalage)

    return chiffré

message = input("Message : ")
decalage = int(input("Nombre de décalage : "))
print(cesar(message, decalage))