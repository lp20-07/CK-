from taikhoan import TaiKhoan

class DanhSachTaiKhoan:
    def __init__(self):
        self.ds_tai_khoan = []
        self.ten_file = "danh_sach_tai_khoan.txt"
        self.doc_du_lieu()

    def doc_du_lieu(self):
        try:
            with open(self.ten_file, "r", encoding="utf-8") as f:
                for dong in f:
                    dong = dong.strip()
                    if not dong: continue
                    du_lieu = dong.split(",")
                    if len(du_lieu) >= 3:
                        sdt = du_lieu[0]
                        mk = du_lieu[1]
                        ten = du_lieu[2]

                        from taikhoan import TaiKhoan
                        tk_moi = TaiKhoan(sdt, mk, ten)
                        self.ds_tai_khoan.append(tk_moi)

            print("Đã đọc dữ liệu cũ thành công!")
        except FileNotFoundError:
            print("Chưa có file dữ liệu, tạo danh sách mới...")
            self.ds_tai_khoan = []

    def luu_them_mot_nguoi(self, tk):
        with open(self.ten_file, "a", encoding="utf-8") as f:
            dong_du_lieu = f"{tk.sdt},{tk.mat_khau},{tk.ho_ten}\n"
            f.write(dong_du_lieu)


    def them_moi(self, tai_khoan):
        for tk in self.ds_tai_khoan:
            if tk.sdt == tai_khoan.sdt:
                return False
        self.ds_tai_khoan.append(tai_khoan)
        self.luu_them_mot_nguoi(tai_khoan)
        return True

    def kiem_tra_dang_nhap(self, sdt, mat_khau):
        for tk in self.ds_tai_khoan:
            if tk.sdt == sdt and tk.mat_khau == mat_khau:
                return tk
        return None

    def tim_kiem_mk(self, thong_tin):
        for tk in self.ds_tai_khoan:
            if tk.sdt == thong_tin or tk.email == thong_tin:
                return tk.mat_khau
        return None

