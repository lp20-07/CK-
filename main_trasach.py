import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QPushButton, QInputDialog, QWidget, QHBoxLayout
from PyQt6 import uic
from PyQt6.QtCore import QDate


class ReturnBookWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("giaodien_trasach.ui", self)


        self.tblSachMuon.setColumnWidth(0, 80)  # Mã sách nhỏ thôi
        self.tblSachMuon.setColumnWidth(1, 200)  # Tên sách dài ra
        self.tblSachMuon.setColumnWidth(2, 150)  # Tình trạng
        self.btnquaylai_2.clicked.connect(self.ve_menu)

        self.ds_sach = []
        self.load_du_lieu_tu_file()

    def load_du_lieu_tu_file(self):
        self.ds_sach = []
        self.tblSachMuon.setRowCount(0)

        try:
            with open("sach_dang_muon.txt", "r", encoding="utf-8") as f:
                for dong in f:
                    dong = dong.strip()
                    if not dong: continue
                    data = dong.split(",")
                    if len(data) >= 3:
                        self.ds_sach.append(data)
            self.hien_thi_len_bang()

        except FileNotFoundError:
            pass

    def hien_thi_len_bang(self):
        self.tblSachMuon.setRowCount(len(self.ds_sach))
        hom_nay = QDate.currentDate()

        for i, sach in enumerate(self.ds_sach):
            self.tblSachMuon.setItem(i, 0, QTableWidgetItem(sach[0]))
            self.tblSachMuon.setItem(i, 1, QTableWidgetItem(sach[1]))
            ngay_tra_str = sach[2]
            try:
                q_ngay_tra = QDate.fromString(ngay_tra_str, "dd/MM/yyyy")
                so_ngay = hom_nay.daysTo(q_ngay_tra)

                if so_ngay < 0:
                    tinh_trang = f"QUÁ HẠN {abs(so_ngay)} ngày!"
                    mau_chu = "color: red; font-weight: bold;"
                elif so_ngay == 0:
                    tinh_trang = "Hạn chót hôm nay"
                    mau_chu = "color: orange;"
                else:
                    tinh_trang = f"Còn {so_ngay} ngày"
                    mau_chu = "color: green;"
            except:
                tinh_trang = "Lỗi ngày"
                mau_chu = "color: black;"

            item_tinh_trang = QTableWidgetItem(tinh_trang)
            self.tblSachMuon.setItem(i, 2, item_tinh_trang)

            btn_tra = QPushButton("Trả")
            btn_tra.setStyleSheet("background-color: #ffcccc; color: red;")
            # Kỹ thuật Lambda: Gắn số dòng (i) vào nút để biết đang bấm dòng nào
            btn_tra.clicked.connect(lambda _, row=i: self.xu_ly_tra(row))
            self.tblSachMuon.setCellWidget(i, 3, btn_tra)


            btn_gia_han = QPushButton("Gia hạn")
            btn_gia_han.setStyleSheet("background-color: #ccffcc; color: green;")
            btn_gia_han.clicked.connect(lambda _, row=i: self.xu_ly_gia_han(row))
            self.tblSachMuon.setCellWidget(i, 4, btn_gia_han)

    def luu_lai_file(self):
        try:
            with open("sach_dang_muon.txt", "w", encoding="utf-8") as f:
                for sach in self.ds_sach:
                    f.write(f"{sach[0]},{sach[1]},{sach[2]},{sach[3]}\n")
        except:
            pass

    def xu_ly_tra(self, row_index):
        if row_index < 0 or row_index >= len(self.ds_sach):
            return
        # self.ds_sach[row_index] là một list gồm: [Mã, Tên, Ngày Mượn, Tình Trạng...]
        ma_sach = self.ds_sach[row_index][0]
        ten_sach = self.ds_sach[row_index][1]

        # Lấy ngày hôm nay làm "Ngày trả thực tế"
        ngay_tra_thuc_te = QDate.currentDate().toString("dd/MM/yyyy")

        hoi = QMessageBox.question(self, "Xác nhận trả",
                                   f"Khách muốn trả sách: {ten_sach}?\nMã: {ma_sach}",
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if hoi == QMessageBox.StandardButton.Yes:
            try:
                with open("lich_su_tra.txt", "a", encoding="utf-8") as f:
                    f.write(f"{ma_sach},{ten_sach},{ngay_tra_thuc_te}\n")
                print("Đã lưu lịch sử thành công!")  # In ra console để kiểm tra
            except Exception as e:
                print(f"Lỗi không lưu được lịch sử: {e}")
                QMessageBox.warning(self, "Lỗi Ghi File", f"Không lưu được lịch sử: {e}")

            del self.ds_sach[row_index]

            self.luu_lai_file()
            self.hien_thi_len_bang()

            QMessageBox.information(self, "Thành công", "Đã trả sách và lưu vào lịch sử!")

    def xu_ly_gia_han(self, index):
            ten_sach = self.ds_sach[index][1]
            ngay_cu_str = self.ds_sach[index][2]
            so_ngay, ok = QInputDialog.getInt(self, "Gia hạn",
                                              f"Sách: {ten_sach}\nNhập số ngày (1-7):",
                                              3, 1, 7)

            if ok:
                don_gia = 2000
                thanh_tien = so_ngay * don_gia

                hoi = QMessageBox.question(self, "Thu phí",
                                           f"Phí gia hạn: {thanh_tien} VNĐ\nĐồng ý gia hạn không?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

                if hoi == QMessageBox.StandardButton.Yes:
                    try:
                        q_ngay_cu = QDate.fromString(ngay_cu_str, "dd/MM/yyyy")

                        if not q_ngay_cu.isValid():
                            raise ValueError(f"Ngày trả hiện tại '{ngay_cu_str}' bị lỗi định dạng!")

                        q_ngay_moi = q_ngay_cu.addDays(so_ngay)

                        self.ds_sach[index][2] = q_ngay_moi.toString("dd/MM/yyyy")
                        self.luu_lai_file()
                        self.hien_thi_len_bang()

                        QMessageBox.information(self, "Thành công", f"Đã gia hạn đến: {self.ds_sach[index][2]}")

                    except ValueError as ve:
                        QMessageBox.warning(self, "Lỗi Ngày Tháng", str(ve))


    def ve_menu(self):
        self.close()
        try:
            from main_manhinhchinh import MainWindow
            self.mh = MainWindow()
            self.mh.show()
        except:
            pass

    def load_du_lieu_tu_file(self):
        self.ds_sach = []
        try:
            with open("sach_dang_muon.txt", "r", encoding="utf-8") as f:
                for dong in f:
                    dong = dong.strip()
                    if not dong: continue

                    data = dong.split(",")

                    if len(data) >= 3:
                        self.ds_sach.append(data)

            self.hien_thi_len_bang()
        except FileNotFoundError:
            pass  # Chưa có ai mượn thì thôi, không báo lỗi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReturnBookWindow()
    window.show()
    sys.exit(app.exec())