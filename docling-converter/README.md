# docling-converter

> **Note:** Docling already ships with a built-in CLI at `.venv/bin/docling` that covers this use case. This project is a demonstration of how to use the Docling library programmatically — it is not intended as a replacement or required tool.
>
> ```bash
> .venv/bin/docling rate-sheets-chase-ma.pdf
> ```

CLI tool to convert documents to Markdown using [Docling](https://github.com/docling-project/docling).

Supports PDF, DOCX, PPTX, XLSX, HTML, and images.

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
git clone <repo>
cd docling-converter
uv sync
```

## Usage

```bash
uv run convert-to-md <input_file>
```

The output is saved as `<input_file>.md` in the same directory by default.

To specify a custom output path:

```bash
uv run convert-to-md <input_file> --output <output_file.md>
```

### Examples

```bash
# Convert a PDF
uv run convert-to-md report.pdf

# Convert a real-world PDF example
uv run convert-to-md rate-sheets-chase-ma.pdf

# Convert a Word document with a custom output path
uv run convert-to-md document.docx -o converted/document.md

# Convert a PowerPoint presentation
uv run convert-to-md slides.pptx
```

### Options

| Option     | Short | Description                                  |
| ---------- | ----- | -------------------------------------------- |
| `--output` | `-o`  | Output file path. Defaults to `<input>.md`   |
| `--help`   |       | Show help and exit                           |
