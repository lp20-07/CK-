import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PyQt6 import uic

class CustomerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("giaodien_dangnhap.ui", self)
        self.danh_sach_tai_khoan = []
        self.stackedWidget.setCurrentIndex(0)

        self.txtmk.setEchoMode(QLineEdit.EchoMode.Password)  # 2 là chế độ Password

        # Từ Đăng nhập -> Sang Đăng ký (Trang 1)
        self.btndangki.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        # Từ Đăng nhập -> Sang Quên MK (Trang 2)
        self.btnquenmk.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        # Các nút "Quay lại" -> Về Đăng nhập (Trang 0)
        self.btnquaylai.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btnquaylai2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.btndangnhap.clicked.connect(self.xu_ly_dang_nhap)
        self.btnxacnhandk.clicked.connect(self.xu_ly_dang_ky)
        self.btnxacthuc.clicked.connect(self.xu_ly_quen_mk)

    def xu_ly_dang_nhap(self):
        sdt = self.txtsdt.text()
        mk = self.txtmk.text()
        tim_thay = False

        for tk in self.danh_sach_tai_khoan:
            if sdt == tk["sdt"] and mk == tk["mk"]:
                tim_thay = True
                ten_nguoi_dung = tk["ten"]
                break
        if tim_thay:
            QMessageBox.information(self, "Thông báo", "Đăng nhập thành công!")

        else:
            QMessageBox.warning(self, "Lỗi", "Sai SĐT hoặc Mật khẩu rồi!")

    def xu_ly_dang_ky(self):
        hoten = self.txthoten.text()
        sdt = self.txtsdt2.text()
        cmt = self.txtcmt.text()
        mk = self.txtmk2.text()
        gmail = self.txtgmail.text()
        tai_khoan_moi = {"sdt": sdt, "mk": mk, "ten": hoten}
        self.danh_sach_tai_khoan.append(tai_khoan_moi)
        QMessageBox.information(self, "Chúc mừng", f"Đã tạo tài khoản cho: {hoten}")
        self.stackedWidget.setCurrentIndex(0)

    def xu_ly_quen_mk(self):
        thong_tin_nhap = self.txtsdt3.text()
        tim_thay = False
        mat_khau_hien_tai = ""

        for tk in self.danh_sach_tai_khoan:
            if tk["sdt"] == thong_tin_nhap or tk.get("gmail") == thong_tin_nhap:
                tim_thay = True
                mat_khau_hien_tai = tk["mk"]

        if tim_thay:
            QMessageBox.information(self, "Lấy lại mật khẩu",
                                    f"Mật khẩu của bạn là: {mat_khau_hien_tai}\n(Hãy ghi nhớ nhé!)")

            self.stackedWidget.setCurrentIndex(0)
        else:
            QMessageBox.critical(self, "Lỗi", "Tài khoản này không tồn tại trong hệ thống!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomerWindow()
    window.show()
    sys.exit(app.exec())