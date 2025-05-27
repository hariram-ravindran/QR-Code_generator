import unittest
import qrcode
import os

class TestQRCodeGenerator(unittest.TestCase):
    def setUp(self):
        self.input_URL = "https://www.google.com/"
        self.output_file = "url_qrcode.png"

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

def test_generate_qr_code(self):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )
    qr.add_data(self.input_URL)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="red", back_color="white")
    img.save(self.output_file)
    
    self.assertTrue(os.path.exists(self.output_file))
    self.assertTrue(os.path.getsize(self.output_file) > 0)
    
    # Verify the QR code content
    decoded_qr = qrcode.QRCode()
    decoded_qr.add_data(self.input_URL)
    self.assertEqual(qr.data_list, decoded_qr.data_list)

if __name__ == '__main__':
    unittest.main()
