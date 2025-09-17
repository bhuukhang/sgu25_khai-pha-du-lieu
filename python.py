import matplotlib.pyplot as plt

# Dữ liệu
bai_tap = ['BT1', 'BT2', 'BT3', 'BT4', 'BT5']
diem = [8, 7.5, 9, 6, 8.5]

# Tạo biểu đồ đường
plt.plot(bai_tap, diem, marker='o', color='blue', linestyle='-', label='Điểm số')

# Thêm tiêu đề và nhãn trục
plt.title("Điểm số các bài tập")
plt.xlabel("Bài tập")
plt.ylabel("Điểm")

# Hiển thị lưới
plt.grid(True)

# Hiển thị legend
plt.legend()

# Hiển thị biểu đồ
plt.show()