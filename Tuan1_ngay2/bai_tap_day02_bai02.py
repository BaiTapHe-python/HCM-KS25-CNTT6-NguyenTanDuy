# Dataset sinh viên
students = [
    {
        "id": "SV01",
        "name": "  Nguyen Van An  ",
        "email": " an.nguyen@rikkei.edu.vn ",
        "phone": " 0987654321 "
    },
    {
        "id": "SV02",
        "name": " Tran Thi Bich ",
        "email": " bich_gmail.com ",
        "phone": " 0912345678 "
    },
    {
        "id": "SV03",
        "name": " Le Hoang Cuong ",
        "email": " cuong@gmail.com ",
        "phone": " 09876abcde "
    },
    {
        "id": "SV04",
        "name": " Pham Minh Dung ",
        "email": " dung@gmail.com ",
        "phone": " 0355667788 "
    }
]

for student in students:
    # Chuẩn hóa dữ liệu
    name = student["name"].strip()
    email = student["email"].strip()
    phone = student["phone"].strip()

    errors = []

    # Validate Email
    if email.count("@") != 1:
        errors.append("Thieu @")
    elif not (email.endswith(".com") or email.endswith(".edu.vn")):
        errors.append("Email sai dinh dang")

    # Validate SĐT
    if not phone.isdigit():
        errors.append("SDT chua chu")
    elif len(phone) != 10:
        errors.append("SDT khong du 10 so")
    elif not phone.startswith("0"):
        errors.append("SDT khong bat dau bang 0")

    # In kết quả
    if len(errors) == 0:
        print(f"[{student['id']}] {name} | Email: {email} | SDT: {phone} -> HO SO HOP LE")
    else:
        print(f"[{student['id']}] {name} | Email: {email} | SDT: {phone} -> KHONG HOP LE ({', '.join(errors)})")