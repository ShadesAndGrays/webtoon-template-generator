# Webtoon Template Generator

A Python-based utility to generate layout grids for Webtoon production. This tool creates a large canvas divided into columns and rows, representing multiple "pages" with customizable gaps, margins, and sub-divisions for better panel planning.

## 2x2 Example
<img src="images\1900x2560-W800xH1280-R2xC2.png" width="350" alt="2x2 Example image">

## 🎯Features
* **Customizable Canvas:** Set page width (standard 800px) and height (standard 1280px).
* **Grid Layout:** Define a specific number of columns and rows.
* **Smart Gaps:** Includes workspace gutters (gaps) between pages to prevent visual clutter.
* **Sub-divisions:** Automatically draws guide lines for vertical and horizontal partitioning.
* **Automated Output:** Saves files with descriptive dimensions into an organized folder.

## 🏢Setup & Installation

1. **Clone or Download** this repository.
2. **Install Dependencies** :
   ```bash
   pip install -r requirements.txt
   ```

## 🚀Usage

1. Open generate-template.py in your code editor.

2. Adjust the variables in the [config.yaml](config.yaml):

    - page_size: The width of a single webtoon page.

    - columns / rows: The total count of pages in your grid.

    - subdivision_amount: How many guide sections you want per page.

3. Run the script:
```bash
python generate-template.py
```

4. Find your generated PNG in the output/templates folder.

## ⚙️ Configuration

You can customize the layout without touching a single line of code by editing config.yaml. The script is designed with "Safety Defaults," meaning if you delete a line or make a mistake, it will automatically fall back to standard Webtoon dimensions

### **Example** `config.yaml`
```yaml
# WEBTOON TEMPLATE CONFIGURATION
# ---------------------------------------------------------
# Note: Colors support Hex (e.g., "#ffffff") or RGBA (e.g., "#ff000030")
# the last two digits of RGBA control transparency (00 is clear, ff is solid).

# Core Page Settings
page:
  width: 800             # Standard Webtoon width is 800px
  height: 1280           # Standard Webtoon height per slice
  columns: 5             # How many pages side-by-side
  rows: 3                # How many pages top-to-bottom
  background_color: "#ffffff"
  debug_color: "#ffff0000" # Background color for the page "active area"

# Page Gutters (The workspace buffers on the sides)
gap:
  size: 75               # Width of the safety gutter on each side
  outline_thickness: 1   # Thickness of the gutter border
  outline_color: 'blue'
  color: "#ff000030"     # Left gutter tint
  color2: "#0000ff30"    # Right gutter tint

# Page Divisions (Main horizontal page breaks)
division:
  size: 3                # Thickness of the line between pages
  color: "#00000050"

# Within page divisions (Vertical and horizontal guide lines)
subdivision:
  size: 1                # Thickness of the guide lines
  color: "#00000050"
  amount: 3              # How many sections to split each page into

```

### 📝 Editing the Configuration

The config.yaml file uses a simple key: value format.  

- Comments: Any text following a # is a note for you and is ignored by the script.

- Indentation: Ensure that sub-settings (like width) stay indented under their main category (like page).

- Colors: You can use standard color names like 'blue' or 'red', or Hex codes for precision.