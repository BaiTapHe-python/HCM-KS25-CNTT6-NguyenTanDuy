from fastapi import FastAPI, status

app = FastAPI(
    title="library_managerment"
)

library =  {
"ten_thu_vien": "Thư viện Rikkei",
"dia_chi": "123 Nguyễn Văn Cừ, Hà Nội",
"gio_mo_cua": "08:00 - 21:00"
}


@app.get("/api/v1/library-infor", status_code=status.HTTP_200_OK)
def lib_infor():
    return library