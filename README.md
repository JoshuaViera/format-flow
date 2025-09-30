# Format Flow 📁✨

Format Flow is a simple and powerful command-line tool that automates the process of formatting raw text files. It watches a designated folder and instantly converts new `.txt` files containing markdown into clean, consistently formatted `.html` documents.

### The Pipeline

COMING SOON

## The Problem It Solves

This tool was built to eliminate the friction of manually cleaning up and formatting text copied from sources like LLMs. It saves time and prevents context-switching by creating a "zero-touch" workflow: just save your raw text, and a formatted version appears automatically.

## Key Features

* **📁 Directory Watching:** Actively monitors a folder for new text files.
* **⚙️ Automatic Formatting:** Converts markdown syntax (headings, lists, bold) to clean HTML.
* **🚀 Simple CLI:** Easy-to-use command-line interface to start and manage the tool.
* **📦 Zero Dependencies (after setup):** Runs quietly in the background.

## Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites

* Python 3.8+
* pip

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/](https://github.com/)https://github.com/JoshuaViera/format-flow.git/format-flow.git
    cd format-flow
    ```
2.  **Create and activate a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1.  Place any `.txt` file containing your raw notes (with markdown) into the `input_folder`.
2.  Run the application from the root directory of the project:
    ```sh
    python -m app.main start
    ```
3.  The tool will start watching the `input_folder`. Any new `.txt` files you save there will be automatically formatted and appear in the `output_folder`.
4.  Press `Ctrl+C` in the terminal to stop the watcher.

You can also specify different input and output directories:
```sh
python -m app.main start --input /path/to/my/notes --output /path/to/my/formatted/docs

[Joshua Viera] - 