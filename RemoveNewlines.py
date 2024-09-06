import pyperclip as pc

def remove_newlines():
    text = pc.paste()
    new_text = text.replace('\n', ' ')
    pc.copy(new_text)
    
remove_newlines()