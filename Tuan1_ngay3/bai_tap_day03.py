# Dataset inventory & students:
inventory = [
    {"id": "SP1", "ten": "Tai nghe Sony", "gia": 1200000, "danh_muc": "Phụ kiện"},
    {"id": "SP2", "ten": "Chuột không dây", "gia": 450000, "danh_muc": "Phụ kiện"},
    {"id": "SP3", "ten": "Bàn phím Cơ", "gia": 950000, "danh_muc": "Phụ kiện"},
    {"id": "SP4", "ten": "Màn hình Dell 27 inch", "gia": 4500000, "danh_muc": "Thiết bị"},
    {"id": "SP5", "ten": "Sạc dự phòng 20000mAh", "gia": 350000, "danh_muc": "Phụ kiện"}
]

students = [
    {"name": "An", "gpa": 7.2},
    {"name": "Bình", "gpa": 9.5},
    {"name": "Cường", "gpa": 6.8},
    {"name": "Dũng", "gpa": 8.4}
]


def linear_search_filter(cart, target_category, max_price):
    result = []

    for product in cart:
        if product["gia"] <= max_price and product["danh_muc"] == target_category:
            result.append(product)

    return result


target_category = "Phụ kiện"
max_price = 1000000

products = linear_search_filter(inventory, target_category, max_price)

print("KẾT QUẢ LỌC SẢN PHẨM (LINEAR SEARCH MULTI-CRITERIA)")
print(f"Danh mục tìm kiếm: {target_category} | Giá tối đa: {max_price:,} VNĐ")
print(f"Tìm thấy {len(products)} sản phẩm phù hợp:")

for product in products:
    print(f"  -> [{product['id']}] {product['ten']} | Giá: {product['gia']:,} VNĐ")


n = len(students)

for i in range(n - 1):
    swapped = False

    for j in range(n - 1 - i):
        if students[j]["gpa"] < students[j + 1]["gpa"]:
            students[j], students[j + 1] = students[j + 1], students[j]
            swapped = True

    if not swapped:
        break

print("BẢNG XẾP HẠNG SINH VIÊN (BUBBLE SORT - GPA GIẢM DẦN)")

for i, student in enumerate(students, start=1):
    print(f"Top {i}: {student['name']} - {student['gpa']} điểm")