#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyPDF2 import PdfWriter, PdfReader

# buat objek pdf writer
out = PdfWriter()

# buka file pdf asli
file = PdfReader("D:/SEM 3/SKD/RSA/PDF/V3922040_Rifqy Rivaldi_TIE_IMKTugas8.pdf")

# identifikasi total halaman file
num = len(file.pages)

# program membaca setiap halaman file sesuai halaman yang diidentifikasi
for idx in range(num):
    page = file.pages[idx]
    out.add_page(page)

# masukkan password enkripsi
password = "Mabardulu"

# enkripsi masing-masing halaman
out.encrypt(password)

# buka file enkripsi "myfile_encrypted.pdf"
with open("D:/SEM 3/SKD/RSA/PDF/V3922040_Rifqy Rivaldi_TIE_IMKTugas8.pdf", "wb") as f:
    # simpan pdf
    out.write(f)


# In[ ]:




