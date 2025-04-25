import keyboard
import pyperclip
import time

copied_items = []
active = False

def start_script():
    global active
    active = True
    print("🟢 Script activated. Use Ctrl+C to collect text, Ctrl+V to paste all.")

def stop_script():
    global active
    active = False
    print("🔴 Script deactivated. Copy/paste handling is paused.")

def copy_handler():
    if active:
        keyboard.send('ctrl+c')
        time.sleep(0.1)
        copied_content = pyperclip.paste()
        if copied_content:
            copied_items.append(copied_content)
            print(f"✅ Copied ({len(copied_items)}):", repr(copied_content))

def paste_handler():
    if active and copied_items:
        all_text = '\n'.join(copied_items)
        pyperclip.copy(all_text)
        time.sleep(0.1)
        keyboard.send("ctrl+v")
        print("📤 Pasted all stored items.")
        copied_items.clear()

if __name__ == "__main__":
    print("⚡ Press Ctrl+Shift+S to activate, Ctrl+Shift+X to deactivate.")

    keyboard.add_hotkey('ctrl+shift+s', start_script)
    keyboard.add_hotkey('ctrl+shift+x', stop_script)
    keyboard.add_hotkey('ctrl+c', copy_handler)
    keyboard.add_hotkey('ctrl+v', paste_handler)

    keyboard.wait()
