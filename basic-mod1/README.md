## basic-mode1

Analsisi soal : 
Kita harus melakukan dekripsi file dengan mod 37:
```
350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213 
```

Penyelesaian : 
Menggunakan code berikut ini :
```
number='350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213'.split()


x=[]
for i in number:
    x+=[int(i)%37]


y=''
for i in x:
    if i<=25:
        y+=chr(i+65)
    elif i==36:
        y+='_'
    else:
        y+=str(i-26)


    print('PICOCTF{'+y+'}')
```


Outputnya :

<img src="https://cdn.discordapp.com/attachments/1025213238763327683/1115106007304114196/image.png" />

Flag : picoCTF{R0UND_N_R0UND_ADD17EC2}