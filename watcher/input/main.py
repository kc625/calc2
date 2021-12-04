"""This is our observer program"""
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

if __name__ == "__main__":
    patterns = ["*"]
    IGNORE_PATTERNS = None
    IGNORE_DIRECTORIES = False
    CASE_SENSITIVE = True
    # pylint: disable=line-too-long
    my_event_handler = PatternMatchingEventHandler(patterns, IGNORE_PATTERNS, IGNORE_DIRECTORIES, CASE_SENSITIVE)

def on_created(event):
    """Event for file being created"""
    print(f"A file called {event.src_path} has been created!")

def on_deleted(event):
    """Event for file being deleted"""
    print(f"It appears {event.src_path} has been deleted.")

def on_modified(event):
    """Event for file being modified"""
    print(f"Look, {event.src_path} has been changed.")

def on_moved(event):
    """Event for file being moved"""
    print(f"Someone has moved {event.src_path} to {event.dest_path}.")

my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved

PATH = "."
GO_RECURSIVELY = True
my_observer = Observer()
my_observer.schedule(my_event_handler, PATH, recursive=GO_RECURSIVELY)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
