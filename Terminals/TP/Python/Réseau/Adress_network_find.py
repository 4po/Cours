def etlogique(a,b) :
    x = 0
    sortie = []
    for i in a :
        if i == '0' and b[x] == '0' :
            sortie.append(0)
        elif i == b[x] :
            sortie.append(1)
        else :
            sortie.append(0)
        x = x+1
    sortie = ''.join(map(str, sortie))
    return sortie

def convert(list):
    s = [str(i) for i in list]
    res = "".join(s)
    return(res)

def ip_to_bin(ip) :
    ip_split = ip.split('.')
    ip_bin = []
    for i in ip_split :
        a = bin(int(i))
        a = list(a)
        for i in range(2) :
            a.pop(0)
        for i in range(8-len(a)) :
            a.insert(0 ,0)
        a=convert(a)
        ip_bin.append(a)
    return ip_bin

def masque_to_bin(masque) :
    masque_split = masque.split('.')
    masque_bin = []
    for i in masque_split :
        b = bin(int(i))
        b = list(b)
        for i in range(2) :
            b.pop(0)
        for i in range(8-len(b)) :
            b.insert(0,0)
        b=convert(b)
        masque_bin.append(b)
    return masque_bin

def network_finder(ip,masque) :
    a = masque_to_bin(masque)
    b = ip_to_bin(ip)
    c = []
    d = []
    e = []
    f = []
    x = 0
    for i in a :
         c.append(list(i))
    for i in b :
        d.append(list(i))
    for i in range(4) :
        e.append(etlogique(c[i],d[i]))
    for i in e :
        f.append(int(e[x], 2))
        x = x +1
    s = [str(i) for i in f]
    res = ".".join(s)
    return ("Masque : "+ masque + "\nIP : " + ip + "\nIP Netwotk : " + res)

#Example :
print(network_finder("192.168.101.100" , "255.255.0.0"))
