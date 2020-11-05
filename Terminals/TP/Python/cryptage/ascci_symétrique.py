def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def encrypt_invite(string , alphabet , key) :
    Convert(alphabet)
    Convert(key)
    if len(alphabet) != len(key) :
        print('Longueur Alphabet =/=  longeur de Key !')
    temp = []
    decoded = []
    x = 0
    for k in range(len(alphabet)) :
        temp.append(alphabet[x])
        temp.append(key[x])
        decoded.append(temp)
        temp = []
        x = x + 1
    string = string.lower()
    decipher = ''
    string = Convert(string)
    result = []
    for i in string :
        for j in decoded :
            if i == j[0] :
                result.append(j[1])
    result = ''.join(map(str , result))
    return result

print(encrypt_invite('Salut je suis là' , 'abcdefghijklmnopqrstuvwxyz ' , 'zyxwvutsrqponmlkjihgfedcba '))
