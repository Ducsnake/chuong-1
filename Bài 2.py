class TS:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm môn Toán: "))
        self.diem_ly = float(input("Nhập điểm môn Lý: "))
        self.diem_hoa = float(input("Nhập điểm môn Hoá: "))

    def in_thong_tin(self):
        print(f"Họ tên thí sinh: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_toan}")
        print(f"Điểm Lý: {self.diem_ly}")
        print(f"Điểm Hoá: {self.diem_hoa}")

    def tinh_tong_diem(self):
         return self.diem_toan + self.diem_ly + self.diem_hoa

danh_sach_thisinh = []

# Sử dụng lớp TS để quản lý thông tin của các thí sinh
n = int(input("Nhập số lượng thí sinh: "))
for i in range(n):  
    thi_sinh_1 = TS("", 0.0, 0.0, 0.0)
    thi_sinh_1.nhap_thong_tin()
    thi_sinh_1.in_thong_tin()
    tong_diem = thi_sinh_1.tinh_tong_diem()
    danh_sach_thisinh.append(thi_sinh_1)
print(f"Tổng điểm của thí sinh: {tong_diem}")

danh_sach_thisinh.sort(key=lambda x: x.tinh_tong_diem(), reverse=True)

print("\nDanh sách các thí sinh trúng tuyển:")
print("{:<20} {:<10}".format("Họ Tên", "Điểm"))
for ho_ten, diem in danh_sach_thisinh:

        print("{:<20} {:<10}".format(ho_ten, diem))

diem_chuan = 20
for thi_sinh_1 in danh_sach_trung_tuyen:
    if thi_sinh_1.tong_diem >= diem_chuan:
        thi_sinh_1.in_thong_tin