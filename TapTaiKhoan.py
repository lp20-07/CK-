from taikhoan import TaiKhoan

class DanhSachTaiKhoan:
    def __init__(self):
        self.danh_sach_tai_khoan = []

    def them_moi(self, tai_khoan):
        for tk in self.danh_sach_tai_khoan:
            if tk.sdt == tai_khoan.sdt:
                return False
        self.danh_sach_tai_khoan.append(tai_khoan)
        return True

    def kiem_tra_dang_nhap(self, sdt, mat_khau):
        for tk in self.danh_sach_tai_khoan:
            if tk.sdt == sdt and tk.mat_khau == mat_khau:
                return tk
        return None

    def tim_kiem_mk(self, thong_tin):
        for tk in self.danh_sach_tai_khoan:
            if tk.sdt == thong_tin or tk.email == thong_tin:
                return tk.mat_khau
        return None