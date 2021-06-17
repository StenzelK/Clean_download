'''Remove the junk from downloads folder'''
import os, time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

folder_to_track = 'D:\\Download'

class MyHandler(FileSystemEventHandler):

        name_to_del="scoped_dir"
        def on_modified(self, event):
                for root, dirs, files in os.walk(folder_to_track):
                        for dir in dirs:
                                if dir.startswith(self.name_to_del):
                                        import shutil
                                        shutil.rmtree(os.path.join(root,dir))


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
