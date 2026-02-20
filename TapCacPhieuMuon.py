from phieu_muon_sach import PhieuMuon


class QuanLyMuonSach:
    def __init__(self):
        self.danh_sach_phieu = []

    def tao_phieu_moi(self, hoten, sdt, diachi, tensach, masach, ngay_muon, ngay_tra):
        phieu = PhieuMuon(hoten, sdt, diachi, tensach, masach, ngay_muon, ngay_tra)
        hop_le, thong_bao = phieu.kiem_tra_ngay()

        if not hop_le:
            return False, thong_bao
        self.danh_sach_phieu.append(phieu)
        return True, "Gửi yêu cầu thành công! Vui lòng chờ duyệt."