#hwpToTxt.py
import pyhwp

def hwpToTxt(hwp_file, txt_file):
    hwp = pyhwp.HWPReader(hwp_file)
    plain_text = hwp.to_text()
    with open(txt_file, 'w', encoding='utf-8') as file:
        file.write(plain_text)