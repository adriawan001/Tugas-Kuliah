barang = [ ] 
def menu():
    listmenu = ["1. Tambah barang","2. menghapus", "3. mengedit",
    "4. menampilkan barang" , "5. mengetahui barang", 
    "6. Menampilkan index", "7. keluar"]
    for i in listmenu:
        print(i)
    pilihan = input("masukkan pilihan anda : ")   
    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2" :
         hapus_barang()
    elif pilihan == "3" :
         edit_barang()                  
    elif pilihan == "4" :
         cek_barang()
    elif pilihan == "5" :
         lihat_barang() 
    elif pilihan == "6" :
         cek_index()                          
         
        
def tambah_barang():
     while True :
         tambah = input("masukkan barang anda : ")       
         barang.append(tambah)
         print(barang)
         lanjut = input("tekan Y jika lanjut : ").upper()
         if lanjut == "Y" :
             pass 
         else :
             menu()    
             
def hapus_barang():
    while True :
        hapus = input("masukkan nama barang : ")
        barang.remove(hapus)
        print(barang)
        lanjut = input("tekan Y jika lanjut : ").upper()
        if lanjut == "Y" :
            pass 
        else :
             menu()                         
               
def edit_barang():
    while True :
        edit = input("masukkan nama barang : ")   
        ubah = input("ubah ke : ")
        barang[barang.index(edit)] =  ubah
        print(barang)
        lanjut = input("tekan Y jika lanjut : ").upper()
        if lanjut == "Y" :
            pass 
        else :
            menu() 
                                    
def cek_barang() :
    for i in barang:
        print(i)           
    lanjut = input("tekan enter untuk kembali  : ")
    if lanjut == " " :
       menu()
    else :
       menu()                                                                                                                                                                         
                                                                                                                                                                                    
def lihat_barang():  
    while True :
        cek_barang = input("masukkan nama barang : ")                                                                                                                                                                                  
        if cek_barang in barang :
            print(cek_barang , "tersedia !")                                                                                                                                                                                                   
            lanjut = input("tekan Y jika lanjut : ").upper()
            if lanjut == "Y" :
                pass 
        else :
            menu() 
def cek_index():
    while True :
        cek_barang = input("masukkan nama barang : ")                                                                                                                                                                                  
        if cek_barang in barang :
                print(cek_barang , "tersedia pada indeks :", barang.index(cek_barang))                                                                                                                                                                                                   
                lanjut = input("tekan Y jika lanjut : ").upper()
                if lanjut == "Y" :
                    pass 
        else :
            menu()

menu()