# main.py
import unlock_docx
import docxToTxt
unlock_docx_file = unlock_docx.decrypt_protected_docx("D:/202009list.docx", "fpdlqmffld")
docxToTxt.write_to_text_file(unlock_docx_file, "D:/output.txt")
