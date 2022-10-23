import queue
import threading
from api_request import *
import asyncio
from tkinter import *




# http://effbot.org/zone/tkinter-threads.htm
def periodicGuiUpdate():
    while True:
        try:
            fn = gui_queue.get_nowait()
        except queue.Empty:
            break
        fn()
    root.after(100, periodicGuiUpdate)

# Run the asyncio event loop in a worker thread.
def start_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(updateLoans())
    loop.run_forever()
    threading.Thread(target=start_loop).start()

# Run the GUI main loop in the main thread.
periodicGuiUpdate()
root.mainloop()

# To stop the event loop, call loop.call_soon_threadsafe(loop.stop).
# To start a coroutine from the GUI, call asyncio.run_coroutine_threadsafe