# common.py
def strip_quotes(text):
    if text.startswith('"') and text.endswith('"'):
        return text[1:-1]
    return text