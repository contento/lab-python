import typer
from pathlib import Path
from docling.document_converter import DocumentConverter

app = typer.Typer(help="Convert files to Markdown using Docling.")


@app.command()
def convert(
    input_file: Path = typer.Argument(..., help="Path to the input file to convert."),
    output: Path = typer.Option(None, "--output", "-o", help="Output file path. Defaults to <input>.md"),
):
    if not input_file.exists():
        typer.echo(f"Error: file '{input_file}' not found.", err=True)
        raise typer.Exit(1)

    output_path = output or input_file.with_suffix(".md")

    typer.echo(f"Converting '{input_file}' ...")
    converter = DocumentConverter()
    result = converter.convert(str(input_file))
    markdown = result.document.export_to_markdown()

    output_path.write_text(markdown, encoding="utf-8")
    typer.echo(f"Saved to '{output_path}'")


if __name__ == "__main__":
    app()
