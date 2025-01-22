class Klinik:
    def __init__(self):
        self.antrian = []  # Daftar antrian pasien

    def tambah_pasien(self):
        nama = input("\nMasukkan nama pasien: ")
        umur = int(input("Masukkan umur pasien: "))
        keluhan = input("Masukkan keluhan pasien: ")

        pasien = {'nama': nama, 'umur': umur, 'keluhan': keluhan}
        self.antrian.append(pasien)
        print(f"\nPasien {nama} telah terdaftar dalam antrian.")

    def tampilkan_antrian(self):
        if not self.antrian:
            print("\nAntrian pasien kosong.")
            return

        print("\nDaftar Antrian Pasien:")
        for idx, pasien in enumerate(self.antrian, start=1):
            print(f"{idx}. Nama: {pasien['nama']}, Umur: {pasien['umur']}, Keluhan: {pasien['keluhan']}")

    def panggil_pasien(self):
        if not self.antrian:
            print("\nTidak ada pasien dalam antrian.")
            return

        pasien_dipanggil = self.antrian.pop(0)  # Memanggil pasien pertama dalam antrian
        print(f"\nPasien yang dipanggil: {pasien_dipanggil['nama']}")
        print(f"Umur: {pasien_dipanggil['umur']}, Keluhan: {pasien_dipanggil['keluhan']}")

    def menu(self):
        while True:
            print("\n=== Menu Utama ===")
            print("1. Tambah Pasien ke Antrian")
            print("2. Tampilkan Daftar Antrian")
            print("3. Panggil Pasien")
            print("4. Keluar")

            pilihan = input("Pilih menu (1/2/3/4): ")

            if pilihan == '1':
                self.tambah_pasien()
            elif pilihan == '2':
                self.tampilkan_antrian()
            elif pilihan == '3':
                self.panggil_pasien()
            elif pilihan == '4':
                print("Terima kasih telah menggunakan Sistem Manajemen Antrian Pasien di Klinik.")
                break
            else:
                print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    klinik = Klinik()
    klinik.menu()
