import sys
from PyQt6.QtWidgets import QApplication
from main_giaodien1 import CustomerInfoWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Dữ liệu mẫu
    thong_tin = {
        'hoten': 'Nguyễn Văn A',
        'sdt': '0123456789',
        'cmt': '123456789',
        'tensach': 'Lập trình Python',
        'masach': 'PY001',
        'diachi': 'Hà Nội',
        'ngay_muon': '24/02/2026',
        'ngay_tra': '10/03/2026'
    }
    
    window = CustomerInfoWindow(thong_tin)
    window.show()
    sys.exit(app.exec())