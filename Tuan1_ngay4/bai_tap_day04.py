# Dataset raw_registers & orders:
raw_registers = [
    {"name": "  Nguyen Van An  ", "email": "an.nguyen@gmail.com", "phone": "0987654321"},
    {"name": "Tran Thi Bich", "email": "bich_gmail.com", "phone": "0912345678"},
    {"name": "Le Hoang Cuong", "email": "cuong@rikkei.edu.vn", "phone": "0123456789"},
    {"name": "  Pham Minh Dung ", "email": "dung@gmail.com  ", "phone": "0355667788"}
]

orders = [
    {"id": "DH01", "total": "12500000", "discount_code": "VIP10", "is_vip": True},
    {"id": "DH02", "total": "450000", "discount_code": "INVALID", "is_vip": False},
    {"id": "DH03", "total": "ABC_ERROR", "discount_code": "", "is_vip": False},
    {"id": "DH04", "total": "8500000", "discount_code": "VIP20", "is_vip": True}
]


# bài 1:
def validate_registration_input(name, email, phone):
    clean_name = name.strip()
    clean_email = email.strip().lower()
    clean_phone = phone.strip()

    is_email_valid = "@" in clean_email
    
    valid_prefixes = ("03", "05", "07", "08", "09")
    is_phone_valid = (len(clean_phone) == 10) and (clean_phone.isdigit()) and (clean_phone.startswith(valid_prefixes))
    
    return clean_name, clean_email, is_email_valid, clean_phone, is_phone_valid

print("=== BÁO CÁO KẾT QUẢ VALIDATE THÔNG TIN ===")
for r in raw_registers:
    c_n, c_e, e_ok, c_p, p_ok = validate_registration_input(r["name"], r["email"], r["phone"])
    status = "Trạng thái: HỢP LỆ" if (e_ok and p_ok) else "Trạng thái: KHÔNG HỢP LỆ"
    print(f"[{c_n}] Email: {c_e} | SDT: {c_p} -> {status}")




# bài 2:
def safe_process_invoice(order_id, raw_total, discount_code, is_vip):
    try:
        total = float(raw_total)

        discount = 0

        if is_vip:
            if discount_code == "VIP10":
                discount = total * 0.10
            elif discount_code == "VIP20":
                discount = total * 0.20

        after_discount = total - discount
        vat = after_discount * 0.10
        final_total = after_discount + vat

        if final_total >= 10000000:
            category = "HÓA ĐƠN LỚN (VIP)"
        else:
            category = "HÓA ĐƠN THƯỜNG"

        if discount > 0:
            print(
                f"[{order_id}] Tiền hàng: {total:,.0f} | "
                f"CK ({discount_code}): {discount:,.0f} | "
                f"VAT 10%: {vat:,.0f} -> "
                f"Tổng: {final_total:,.0f} VNĐ [{category}]"
            )
        else:
            print(
                f"[{order_id}] Tiền hàng: {total:,.0f} | "
                f"CK: 0 | "
                f"VAT 10%: {vat:,.0f} -> "
                f"Tổng: {final_total:,.0f} VNĐ [{category}]"
            )

    except ValueError:
        print(f"Xử lý lỗi [{order_id}]: Số tiền '{raw_total}' không hợp lệ! Bỏ qua đơn hàng.")


print("\nBÁO CÁO XỬ LÝ HÓA ĐƠN AN TOÀN (TRY-EXCEPT & VAT)")

for order in orders:
    safe_process_invoice(
        order["id"],
        order["total"],
        order["discount_code"],
        order["is_vip"]
    )


