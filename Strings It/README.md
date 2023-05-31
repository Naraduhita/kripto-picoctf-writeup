
### Strings It

Menemukan flag pada file strings yang diberikan.

- Download file yang diberikan `wget <link>`
- Mengubah permission pada file strings agar dapat menjalankan file `chmod +x strings`
- Menjalankan `stirngs -a strings >> strings.txt`. Perintah "strings" digunakan untuk mengekstraksi teks yang tersembunyi dalam file biner.  `-a` memastikan bahwa semua karakter yang terbaca sebagai teks akan ditampilkan, termasuk karakter yang biasanya tidak dianggap sebagai karakter teks standar. Lalu hasil dari ekstraksi akan disimpan ke strings.txt
- Melakukan pencarian dengan kata kunci pico pada file strings.txt
- Dari hasil pencarian didapatkan flag : `picoCTF{5tRIng5_1T_827aee91}`

<img src="https://github.com/Naraduhita/kripto-picoctf-writeup/assets/102397053/d66a0e38-6c9a-403b-987a-f0318615e71c" height="300" />

<img src="https://github.com/Naraduhita/kripto-picoctf-writeup/assets/102397053/8b1db249-172a-47fc-b9f9-3c2f2f874a6f" height="300" />

