## New Caesar

Pada soal CTF new caesar ini ditemukan jenis enkripsi baru. kita diminta untuk mendeskripsikan chipertext yang diberikan dengan algoritma yang sudah diberi.

Hint 1: Bagaimana cara kerja sandi jika alfabetnya bukan 26 huruf?
Hint 2: Meskipun huruf-hurufnya terpisah, paradigma yang sama masih berlaku

Teknik mengenkripsi karakternya sehingga kita perlu memahani enkripsinya untuk dapat membuat algoritma dekripsinya.

Menggunakan python3
 Mencari nilai loweroffset
 f'{ord("a"):08b}'
Karakter yang akan diolah ternyata dibagi menjadi 2 bagian yakni 4bit awal dan 4bit akhir.
int(a[4:],2) = 6
int(a[:4],2) = 1
Setiap karakter yang nantinya akan dicoba dekripsi akan dikurangi loweroffsetnya.
Cek ALPHABET
print(ALPHABET)
ALPHABET[6]
ALPHABET[1]

enkripsi
a = 97 --> 01100001
dibagi 2 --> 0110 0001 = 6 dan 1
6 =g dan 1 =b 

Deskripsi (kebalikan enkripsi)
gb ==>61 -->01100001 -> 97 -> a


Penjelasan algoritma
LOWERCASE_OFFSET adalah offset numerik untuk menghitung indeks karakter huruf kecil dalam alfabet.
ALPHABET adalah string yang berisi 16 huruf kecil pertama dari alfabet.

n1 dan n2(maju satu karakter karena akan mengambil setiap 2 karakter untuk dideskripsikan)
kemudian 4bit awal n1 akan ditambahkan n2. 
Fungsi shift(c, k) berfungsi melakukan pergeseran terhadap karakter c dengan jumlah yang ditentukan oleh karakter k.
Melakukan loop for untuk mengiterasi setiap karakter dalam ALPHABET sebagai kunci. Setiap kunci digunakan untuk melakukan pergeseran pada setiap karakter dalam string enc

Ketika program dijalankan maka muncul beberapa string hasil dekripsi. Dan setelah dicoba maka didapatkan flag : picoCTF{et_tu?_431db62c5618cd75f1d0b83832b67b46}
