from PIL import Image, ImageDraw, ImageColor
from pathlib import Path
import yaml

## Variaiable
with open('config.yaml', "r") as f:
    config = yaml.safe_load(f) or {}

page  = config.get('page', {})
gap  = config.get('gap', {})

division  = config.get('division', {})
subdivision  = config.get('subdivision', {})

page_size = page.get('width',800)
page_height = page.get('height',1280) 

columns = page.get('columns',6)
rows = page.get('rows',3)

canvas_color = page.get('background_color',"#ffffffff")
page_debug_color = page.get('debug_color',"#ffff0011")

gap_size = gap.get('size',75)
gap_outline_thickness = gap.get('outline_thickness',1)
gap_outline_color = gap.get('outline_color','blue')
gap_color = gap.get('color',"#ff000030")
gap_color2 = gap.get('color2',"#0000ff30")

division_size = division.get('size',3)
division_color = division.get('color',"#00000050")

subdivision_size = subdivision.get('size',1)
subdivision_color = subdivision.get('color',"#00000050")
subdivision_amount = subdivision.get('amount',3)

width, height =  (page_size + gap_size * 2 ) *columns, page_height * rows #4800, 3840 #800 * 6, 1280 * 3


print(f"Width: {width}, Height: {height}")

img = Image.new('RGB', (width,height), color=canvas_color)

draw = ImageDraw.Draw(img,'RGBA')
workspace_size =  page_size + gap_size*2

print("Workspace size: ",workspace_size )

for i in range(int(width/(workspace_size))):
    # Center Regions
    draw.rectangle([
        i*workspace_size+gap_size, 
        0,
        (i+1)* workspace_size-gap_size, 
        height
        ],
        fill=page_debug_color
        )

    page_partition_size = 800/subdivision_amount
    for j in range(1,subdivision_amount):
        draw.line([
            (i*workspace_size) + gap_size + (page_partition_size * j),
            0,
            (i*workspace_size) + gap_size + (page_partition_size * j),
            height
            ],
            fill=subdivision_color,
            width=subdivision_size,
        )


    # Left gap
    draw.rectangle([
        i*workspace_size,
        0,
        (i*workspace_size) + gap_size,
        height
        ],
        fill=gap_color,
        outline=gap_outline_color,
        width=gap_outline_thickness,
    )

    # right gap
    draw.rectangle(
        [
        (i*workspace_size) + page_size + gap_size,
        0,
        (i*workspace_size) + page_size + gap_size*2,
        height
        ],
        fill=gap_color2,
        outline=gap_outline_color,
        width=gap_outline_thickness,
    )

    # Divisions
    for j in range(int(height/page_height)):
        draw.line([
        i*workspace_size,
        j*page_height,
        (i*workspace_size) + page_size + gap_size *2,
        j*page_height,
        ],
        width=division_size,
        fill=division_color
        )

        # Sub-divisions
        if subdivision_amount < 2:
            continue
        start = j*page_height 
        offset = page_height/subdivision_amount
        for k in range(1,subdivision_amount):
            draw.line([
            i*workspace_size,
            start + (offset * k),
            (i*workspace_size) + page_size + gap_size *2,
            start + (offset *k),
            ],
            width=subdivision_size,
            fill=subdivision_color
            )

output_folder  = Path("output/templates")
output_folder.mkdir(parents=True,exist_ok=True)

img.save(output_folder / f'{width}x{height}-W{page_size}xH{page_height}-R{rows}xC{columns}.png')
