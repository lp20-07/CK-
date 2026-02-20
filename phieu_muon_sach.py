from datetime import datetime


class PhieuMuon:
    def __init__(self, hoten, sdt, diachi, tensach, masach, ngay_muon, ngay_tra):
        self.ho_ten = hoten
        self.sdt = sdt
        self.dia_chi = diachi
        self.ten_sach = tensach
        self.ma_sach = masach
        self.ngay_muon = ngay_muon
        self.ngay_tra = ngay_tra

    def kiem_tra_ngay(self):
        fmt = '%d/%m/%Y'
        d_muon = datetime.strptime(self.ngay_muon, fmt)
        d_tra = datetime.strptime(self.ngay_tra, fmt)

        delta = d_tra - d_muon
        so_ngay = delta.days

        if so_ngay < 0:
            return False, "Ngày trả không được nhỏ hơn ngày mượn!"
        if so_ngay > 30:
            return False, f"Bạn mượn {so_ngay} ngày. Quy định tối đa chỉ 30 ngày."

        return True, "Hợp lệ"