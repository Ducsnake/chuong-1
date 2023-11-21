class Hinh_chu_nhat:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

Hinh_chu_nhat = Hinh_chu_nhat(5, 3)  # Khởi tạo hình chữ nhật với chiều dài 5 và chiều rộng 3
area = Hinh_chu_nhat.calculate_area()  # Tính diện tích của hình chữ nhật
perimeter = Hinh_chu_nhat.calculate_perimeter()  # Tính chu vi của hình chữ nhật

print("Độ dài 2 cạnh của hình chữ nhật lần lượt là:", Hinh_chu_nhat.length, Hinh_chu_nhat.width)
print("Diện tích của hình chữ nhật là:", area)
print("Chu vi của hình chữ nhật là:", perimeter)