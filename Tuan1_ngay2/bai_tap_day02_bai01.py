
# Dataset orders:
orders = [
    {"id": "DH01", "name": "iPhone 15 Pro Max", "price": 32000000},
    {"id": "DH02", "name": "Tai nghe AirPods Pro", "price": 5500000},
    {"id": "DH03", "name": "MacBook Pro M3 Max", "price": 65000000},
    {"id": "DH04", "name": "Chuot khong day", "price": 450000},
    {"id": "DH05", "name": "Samsung Galaxy S24", "price": 22000000}
]

total_price = 0
quantity_VIP = 0
orders_max = orders[0]
orders_min = orders[0]
riks = [value for value in orders if value.get("price") > 50000000]

is_suspicious = False

for value in orders:
    total_price += value.get("price")
    if value.get("price")  >= 15000000:
        quantity_VIP += 1
    if value.get("price") > 50000000:
        is_suspicious = True
    if value.get("price") >= orders_max.get("price"):
        orders_max = value
    if value.get("price") <= orders_min.get("price"):
        orders_min = value

print(f"Tong doanh thu: {total_price:,} VNĐ")
print(f"So don hang VIP (>=15tr): {quantity_VIP} don")
print(f"Don hang gia tri CAO NHAT: {orders_max.get("id")} - {orders_max.get("name")} ({orders_max.get("price"):,} VNĐ)")
print(f"Don hang gia tri THAP NHAT: {orders_min.get("id")} - {orders_min.get("name")} ({orders_min.get("price"):,} VNĐ)")
if is_suspicious == True:
    for value in riks:
        print(f"CANH BAO RUI RO: Phat hien don {value.get("id")} co gia tri {value.get("price"):,} VNĐ > 50tr!")

    print("KET LUAN CAM CO: Co is_suspicious = True")



