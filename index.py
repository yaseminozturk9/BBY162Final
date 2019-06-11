#__author__Yasemin Öztürk__


from tkinter import *
class index:
    def __init__(self, anasayfa):
        self.anasayfa = anasayfa
        anasayfa.title("Kütüphane Kataloğu")
        anasayfa.config(bg="lightblue")
        anasayfa.geometry("480x300")

        self.eserleriListele = Button(anasayfa, text="Eserleri Listele", bg="lightblue", width="30",  fg="black",font=("bold", 20), command = self.eserleriListele)
        self.eserleriListele.grid(row="1")

        self.eserEkle = Button(anasayfa, text="Eser Ekle", bg="lightblue",width="30", fg="black", font=("bold", 20), command=self.eserEkle )
        self.eserEkle.grid(row="2")

        self.eserBul = Button(anasayfa, text="Eser Bul", bg="lightblue", width="30", fg="black",font=("bold", 20), command=self.eserBul)
        self.eserBul.grid(row="3")

        self.cikis = Button(anasayfa, text="Çık",bg="lightblue", width="15", fg="black",command=exit,)
        self.cikis.grid(row="4")

    def eserEkle(self):
        global eserAdi, yazarAdi, yayinYili,pencere1
        pencere1 = Tk()
        baslik1 = pencere1.title("Eser Ekle")
        pencere1.config(bg="lightblue")
        eserAdi = Entry(pencere1)
        yazarAdi = Entry(pencere1)
        yayinYili = Entry(pencere1)

        eserAdi.grid(column=2, row=3)
        yazarAdi.grid(column=2, row=4)
        yayinYili.grid(column=2, row=5)



        self.kaydet = Button(pencere1, text= "Kaydet", command= self.eserKaydet, fg="black", bg="lightblue")
        self.kaydet.grid(column=1, row=9)
        Label(pencere1, font="bold", bg="lightblue", text="Eser Ekle").grid(column=1,row=1)
        Label(pencere1, font="bold", bg="lightblue", text="Eser Adı: ").grid(column=1, row=3)
        Label(pencere1, font="bold", bg="lightblue", text="Yazar Adı: ").grid(column=1, row=4)
        Label(pencere1, font="bold", bg="lightblue", text="Yayın Yılı: ").grid(column=1, row=5)

    def eserKaydet(self):
        pencere1 = Tk()
        kayit = str((eserAdi.get()+ ":" + yazarAdi.get()+ ":" + yayinYili.get()+ "\n"))
        dosya = open("kaynak.txt", "a")
        for i in kayit:
            dosya.write(i)
        dosya.close()
        command = pencere1.destroy()

    def eserleriListele(self):
        pencere2 = Tk()
        baslik2 = pencere2.title("Kayıtlı Eserler")
        pencere2.config(bg="lightblue")
        file = open("kaynak.txt")
        data =file.readlines()
        file.close()

        eserListe = Label(pencere2, text=data, fg="black", bg="lightblue",font=("bold",20))
        eserListe.pack()

        cikis = Button(pencere2, text ="Çık",fg="black", bg="lightblue", command=pencere2.destroy )
        cikis.pack()


    def eserBul(self):
        pencere3 = Tk()
        baslik3 = pencere3.title("Eser Bul")
        pencere3.config(bg="lightblue")

        def eser():
            pencere3_1 = Tk()
            baslik2 = pencere3_1.title("Katalog Sonuçları")
            pencere3_1.configure(background="lightblue")
            dosya = open("kaynak.txt", "r")
            deger = dosya.readlines()
            for i in deger:
                if (i.split(':') == eserAdiAl.get()):
                    sonuc = Label(pencere3, bg="lightblue", fg="black", text="\nBulunan Kayıt: " + i)
                    sonuc.grid()
                    break

                else:
                    print("Aranan Kayıt Bulunamadı")
                    dosya.close()

        def yazar():
            pencere3_1 = Tk()
            baslik2 = pencere3_1.title("Katalog Sonuçları")
            pencere3_1.configure(background="lightblue")
            dosya = open("kaynak.txt", "r")
            deger = dosya.readlines()
            for i in deger:
                if (i.split(':') == yazarAdiAl.get()):
                    sonuc = Label(pencere3_1, bg="lightblue", fg="black", text="\nBulunan kayıt: " + i)
                    sonuc.grid()
                    break
                else:
                    print("Aranan Kayıt Bulunamadı")

        def yil():
            pencere3_1 = Tk()
            baslik2 = pencere3_1.title("Katalog Sonuçları")
            pencere3_1.configure(background="lightblue")
            dosya = open("kaynak.txt", "r")
            deger = dosya.readlines()
            for i in deger:
                if (i.split(':') == yilAl.get()):
                    sonuc= Label(pencere3_1, bg="lightblue", fg="black", text="\nBulunan kayıt: " + i)
                    sonuc.grid()
                    print("i")
                    break
                else:
                    print("Aranan kayıt bulunamadı.")




        eserAdi = Label(pencere3, bg="lightblue", fg="black",font="16", text="Eser adı ile tarama ")
        eserAdi.grid(row=0, column=0)
        eserAdiAl = Entry(pencere3, width="30")
        eserAdiAl.grid(row=0, column=1)
        tusAra = Button(pencere3, text="ara", bg="lightblue", fg="black", command=eser)
        tusAra.grid(row=0, column=2)

        yazarAdi = Label(pencere3,bg="lightblue", fg="black",font="16", text="Yazar adı ile tarama ")
        yazarAdi.grid(row=1, column=0)
        yazarAdiAl = Entry(pencere3, width="30")
        yazarAdiAl.grid(row=1, column=1)
        tusAra = Button(pencere3, text="ara", bg="lightblue", fg="black", command=yazar)
        tusAra.grid(row=1, column=2)

        yil = Label(pencere3, bg="lightblue", fg="black", font="16", text="Yayın yılı ile tarama ")
        yil.grid(row=2, column=0)
        yilAl = Entry(pencere3, width="30")
        yilAl.grid(row=2, column=1)
        tusAra = Button(pencere3, text="ara", bg="lightblue", fg="black", command=yil)
        tusAra.grid(row=2, column=2)

root = Tk()
yeniPencere = index(root)
root.mainloop()



