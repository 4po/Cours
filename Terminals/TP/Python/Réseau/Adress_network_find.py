def etlogique(a,b) :
    x = 0
    sortie = []
    for i in a :
        if i == b[x] :
            sortie.append('1')
        else :
            sortie.append('0')
        x+1
        sortie = "".join(sortie)

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def convert2(list):
    s = [str(i) for i in list]
    res = "".join(s)
    return(res)

def convert3(list):
    s = [str(i) for i in list]
    res = ".".join(s)
    return(res)

def ip_to_bin(ip) :
    ip_split = ip.split('.')
    ip_bin = []
    for i in ip_split :
        a = bin(int(i))
        a = Convert(a)
        for i in range(2) :
            a.pop(0)
        for i in range(8-len(a)) :
            a.insert(0 ,0)
        a=convert2(a)
        ip_bin.append(a)
    return ip_bin

def masque_to_bin(masque) :
    masque_split = masque.split('.')
    masque_bin = []
    for i in masque_split :
        b = bin(int(i))
        b = Convert(b)
        for i in range(2) :
            b.pop(0)
        for i in range(8-len(b)) :
            b.insert(0,0)
        b=convert2(b)
        masque_bin.append(b)
    return masque_bin

def network_finder(ip,masque) :
    a = masque_to_bin(masque)
    b = ip_to_bin(ip)
    c = []
    d = []
    e = []
    x = 0
    for i in a :
         c.append(list(i))
    for i in b :
        d.append(list(i))
    for i in range(8) :
        e = etlogique(c,d)
    return e
print(network_finder("197.0.25.96" , "255.255.255.224"))
