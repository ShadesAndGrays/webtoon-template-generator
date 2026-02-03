from PIL import Image
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

gap_size = gap.get('size',75)


splitter  = config.get('splitter', {})
file_path  = splitter.get('file_path', "")
start_index  = splitter.get('start_index', 0)
limit  = splitter.get('limit', -1)
ouput_format = splitter.get('format', "jpeg")
ouput_quality = splitter.get('quality', 90)



if file_path == "":
    print("Invalid file path: ", file_path )
    exit(1)

final_image = Path(file_path)
if not final_image.exists():
    print(f"Final image \"{final_image}\" does not exist")
    exit(1)


out_folder_path = ("output/final_pages")
out_folder_path += "/" + final_image.stem

out_folder = Path(out_folder_path)
out_folder.mkdir(parents=True,exist_ok=True)

Image.init()
img = Image.open(final_image)

workspace_size = (page_size + gap_size * 2)  

stop = False
for c in range(columns):
    for r in range(rows):

        if limit > 0 and start_index+r+(c*rows) + 1 > limit:
            stop = True
            break

        left = (c * workspace_size) + gap_size
        top =  r * page_height
        right = left + page_size 
        bottom = top + page_height

        page = img.crop((left, top, right, bottom))
        output_idx = start_index+r+(c*rows)
        output_name = f"{output_idx:04d}.{ouput_format}"
        print(f"Saving {output_name}")

        match ouput_format:
            case "jpeg":
                final_page = page.convert("RGB")
                final_page.save(out_folder / output_name,"JPEG", quality=ouput_quality )
            case "png":
                final_page.save(out_folder / output_name,"PNG")
            case _:
                final_page.save(out_folder / output_name,"JPEG", quality=ouput_quality )


    if stop:
        break

