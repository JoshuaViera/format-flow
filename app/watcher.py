import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from . import formatter # Use a relative import

class FormatFileHandler(FileSystemEventHandler):
    """
    A handler for file system events that formats new text files.
    """
    def __init__(self, output_dir: str):
        self.output_dir = output_dir

    def on_created(self, event):
        # Ignore directory creation events
        if event.is_directory:
            return

        # Process only .txt files
        if event.src_path.endswith(".txt"):
            print(f"✅ New file detected: {event.src_path}")
            
            # Wait a moment to ensure the file is fully written before reading
            time.sleep(1)
            
            try:
                with open(event.src_path, 'r', encoding='utf-8') as f:
                    messy_text = f.read()

                # Format the text using our formatter engine
                clean_html = formatter.format_llm_text(messy_text)

                # Create the new filename
                base_filename = os.path.basename(event.src_path)
                new_filename = base_filename.replace('.txt', '_formatted.html')
                output_path = os.path.join(self.output_dir, new_filename)

                # Write the formatted HTML to the output directory
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(clean_html)
                print(f"📄 Formatted file saved to: {output_path}")

            except Exception as e:
                print(f"❌ Error processing {event.src_path}: {e}")


def run(input_dir: str, output_dir: str):
    """
    Initializes and runs the file system watcher.

    Args:
        input_dir: The directory to watch for new files.
        output_dir: The directory to save formatted files.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    event_handler = FormatFileHandler(output_dir=output_dir)
    observer = Observer()
    observer.schedule(event_handler, input_dir, recursive=False)
    
    print(f"👀 Watching folder: '{os.path.abspath(input_dir)}'")
    print(f"💾 Output will be saved in: '{os.path.abspath(output_dir)}'")
    print("Press Ctrl+C to stop.")

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Watcher stopped.")
    observer.join()