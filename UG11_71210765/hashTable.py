class RakBuku:
    def __init__(self,size):
        self.size = size
        self.map = [None] * self.size

    def getHash(self,key):
        sum = 0
        for char in key:
            sum += sum *37+ord(char)
        return sum % self.size

    def probing(self,key):
        for index in range(self.size):
            probeHash = self.linearProbing(key, index)
            if (self.map[probeHash] is None) or (self.map[probeHash] == 'deleted'):
                return probeHash

    def linearProbing(self,key,index):
        return (self.getHash(key)+index) % self.size

    def tambahBuku(self,jenisBuku,namaBuku):
        hash_key = self.getHash(jenisBuku)
        key_value = [jenisBuku,namaBuku]
        if self.map[hash_key] is None:
            self.map[hash_key] = list([key_value])
            # print(jenisBuku,'masuk!')
            return True
        else:
            hash_key = self.probing(jenisBuku)
            if hash_key is None:
                print('Rak Buku anda sudah penuh')
                return False
            else:
                self.map[hash_key] = list([key_value])
                # print(key,'masuk!')
                return True

    def lihatBuku(self,jenisBuku):
        hash_key = self.getHash(jenisBuku)
        if (self.map[hash_key] is not None) and (self.map[hash_key] != 'deleted'):
            for index in range(self.size):
                hash_key = self.linearProbing(jenisBuku,index)
                if(self.map[hash_key][0][0] == jenisBuku):
                    return self.map[hash_key][0][1]
        print("Key",jenisBuku,'tidak ditemukan')
        return 'None'
    
    def ambilBuku(self,jenisBuku):
        hash_key = self.getHash(jenisBuku)
        if self.map[hash_key] is None:
            return False
        else:
            for index in range(self.size):
                hash_key = self.linearProbing(jenisBuku,index)
                if self.map[hash_key][0][0] == jenisBuku:
                    self.map[hash_key] = 'deleted'
                    print('deleting',jenisBuku)
                    return True
        print('Key',jenisBuku,'tidak ditemukan')
        return False

    def printAll(self):
        print('====================== List Buku ===================')
        for item in self.map:
            if (item is not None) and (item != 'deleted'):
                print('Nama :',item[0][1],'<> Jenis :',item[0][0])
        print('====================================================')

if __name__ == "__main__":
    rak1 = RakBuku(5)
    rak1.tambahBuku("History", "Mein Kampf (B01)")
    rak1.tambahBuku("Fantasy", "The Witcher (B02)")
    rak1.tambahBuku("Mystery", "Exile (B03)")
    rak1.tambahBuku("Sci Fi", "The Martian (B04)")
    rak1.tambahBuku("History", "World War (B05)")
    rak1.tambahBuku("Romance", "Twilight (B06)")
    print(rak1.lihatBuku("History"))
    print(rak1.lihatBuku("Romance"))
    rak1.ambilBuku("Sci Fi")
    rak1.ambilBuku("Romance")
    rak1.printAll()