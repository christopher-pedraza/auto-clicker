import keyboard
import threading
import time

# Flag to control the writing thread
keep_writing = False


def write_ones():
    global keep_writing
    while keep_writing:
        keyboard.write("1", delay=0.3)
        # time.sleep(0.3)


def start_writing(e):
    global keep_writing
    keep_writing = True
    threading.Thread(target=write_ones).start()


def stop_writing(e):
    global keep_writing
    keep_writing = False


keyboard.on_press_key("x", start_writing)
keyboard.on_press_key("esc", stop_writing)

# Block forever, the script is exited by pressing 'esc'
keyboard.wait()
