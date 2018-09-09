import time
import pyperclip

txtToSave = ''

while True:
    time.sleep(0.1)
    txtClipboard = pyperclip.paste()
    if txtToSave != txtClipboard:
        txtToSave = txtClipboard
        with open('clipboard.txt', 'a') as f:
            f.write(txtToSave + '\n' + '\n' + '\n')