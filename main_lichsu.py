import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QMessageBox
from PyQt6 import uic


class HistoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("giaodien_lichsu.ui", self)


        self.tbllichsu.setColumnWidth(0, 100)  # Mã
        self.tbllichsu.setColumnWidth(1, 300)  # Tên (để rộng ra cho đẹp)
        self.tbllichsu.setColumnWidth(2, 150)  # Ngày trả
        self.tbllichsu.setColumnWidth(3, 100)  # Cột chứa nút bấm
        self.btnquaylai.clicked.connect(self.ve_menu)
        self.load_lich_su()

    def load_lich_su(self):
        self.tbllichsu.setRowCount(0)
        self.du_lieu = []

        try:
            with open("lich_su_tra.txt", "r", encoding="utf-8") as f:
                for dong in f:
                    dong = dong.strip()
                    if not dong: continue
                    parts = dong.split(",")
                    if len(parts) >= 3:
                        self.du_lieu.append(parts)
        except FileNotFoundError:
            return  # Chưa có lịch sử thì thôi
        self.du_lieu.reverse()

        self.tbllichsu.setRowCount(len(self.du_lieu))
        for i, row_data in enumerate(self.du_lieu):
            self.tbllichsu.setItem(i, 0, QTableWidgetItem(row_data[0]))  # Mã
            self.tbllichsu.setItem(i, 1, QTableWidgetItem(row_data[1]))  # Tên
            self.tbllichsu.setItem(i, 2, QTableWidgetItem(row_data[2]))  # Ngày trả

        self.hien_thi_len_bang()

    def hien_thi_len_bang(self):
        self.tbllichsu.setRowCount(len(self.du_lieu))
        for i, row_data in enumerate(self.du_lieu):
            # Dữ liệu: row_data[0]=Mã, row_data[1]=Tên, row_data[2]=Ngày Trả
            self.tbllichsu.setItem(i, 0, QTableWidgetItem(row_data[1]))  # Cột 0: Tên sách
            self.tbllichsu.setItem(i, 1, QTableWidgetItem(row_data[0]))  # Cột 1: Mã sách
            self.tbllichsu.setItem(i, 2, QTableWidgetItem(row_data[2]))  # Cột 2: Ngày trả

            btn_xem = QPushButton("Xem chi tiết")
            btn_xem.setStyleSheet("background-color: #3498db; color: white; font-weight: bold;")

            btn_xem.clicked.connect(lambda _, r=i: self.xem_phieu(r))

            self.tbllichsu.setCellWidget(i, 3, btn_xem)

    def xem_phieu(self, row_index):
        data = self.du_lieu[row_index]
        ma_sach = data[0]
        ten_sach = data[1]
        ngay_tra = data[2]
        noi_dung = (
            "----------------------------------------\n"
            "       HÓA ĐƠN TRẢ SÁCH       \n"
            "----------------------------------------\n\n"
            f" Tên sách:  {ten_sach}\n"
            f" Mã sách:   {ma_sach}\n"
            f" Ngày trả:  {ngay_tra}\n\n"
            "----------------------------------------\n"
            "   Trạng thái: ĐÃ HOÀN TẤT   \n"
            "   Cảm ơn quý khách!         \n"
            "----------------------------------------"
        )
        QMessageBox.information(self, "Phiếu Mượn Chi Tiết", noi_dung)

    def ve_menu(self):
        from main_manhinhchinh import MainWindow
        self.mh = MainWindow()
        self.mh.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HistoryWindow()
    window.show()
    sys.exit(app.exec())