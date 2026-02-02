# Webtoon Template Generator

A Python-based utility to generate layout grids for Webtoon production. This tool creates a large canvas divided into columns and rows, representing multiple "pages" with customizable gaps, margins, and sub-divisions for better panel planning.

## Features
* **Customizable Canvas:** Set page width (standard 800px) and height (standard 1280px).
* **Grid Layout:** Define a specific number of columns and rows.
* **Smart Gaps:** Includes workspace gutters (gaps) between pages to prevent visual clutter.
* **Sub-divisions:** Automatically draws guide lines for vertical and horizontal partitioning.
* **Automated Output:** Saves files with descriptive dimensions into an organized folder.

## Setup & Installation

1. **Clone or Download** this repository.
2. **Install Dependencies** :
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open generate-template.py in your code editor.

2. Adjust the variables in the ## Variaiable section:

    - page_size: The width of a single webtoon page.

    - columns / rows: The total count of pages in your grid.

    - subdivision_amount: How many guide sections you want per page.

3. Run the script:
```bash
python generate-template.py
```

4. Find your generated PNG in the output/templates folder.