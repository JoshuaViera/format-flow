import typer
import os
from . import watcher

# Create a Typer application instance
app = typer.Typer(
    name="Format Flow",
    help="A CLI tool to automatically format text files from a watched folder."
)

@app.command()
def start(
    input_dir: str = typer.Option(
        "input_folder",
        "--input",
        "-i",
        help="The directory to watch for new .txt files."
    ),
    output_dir: str = typer.Option(
        "output_folder",
        "--output",
        "-o",
        help="The directory where formatted .html files will be saved."
    )
):
    """
    Starts the Format Flow file watcher on the specified directories.
    """
    # Use typer.style for colored and bold output in the terminal
    input_path = os.path.abspath(input_dir)
    output_path = os.path.abspath(output_dir)

    typer.secho("🚀 Starting Format Flow...", fg=typer.colors.CYAN, bold=True)
    
    # Check if input directory exists
    if not os.path.isdir(input_path):
        typer.secho(f"Error: Input directory '{input_path}' not found.", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    # Run the watcher from the watcher module
    watcher.run(input_dir=input_path, output_dir=output_path)


if __name__ == "__main__":
    app()
