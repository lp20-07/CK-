class TaiKhoan:
    def __init__(self, sdt, mat_khau, ho_ten, cmt="", email=""):
        self.sdt = sdt
        self.mat_khau = mat_khau
        self.ho_ten = ho_ten
        self.cmt = cmt
        self.email = email

    def doi_mat_khau(self, mat_khau_moi):
        self.mat_khau = mat_khau_moi

