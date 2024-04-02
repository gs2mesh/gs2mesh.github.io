import os
from PIL import Image

def convert_png_to_jpeg(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(".png"):
                full_path = os.path.join(root, file)
                im = Image.open(full_path)
                
                # Create a white background image
                white_bg = Image.new("RGB", im.size, (255, 255, 255))
                # Paste the image onto the white background, using itself as a mask for transparency
                white_bg.paste(im, mask=im.split()[3] if im.mode == 'RGBA' else None)
                
                jpeg_path = full_path.rsplit('.', 1)[0] + '.jpeg'
                white_bg.save(jpeg_path, "JPEG")
                
                os.remove(full_path)
                print(f"Converted and removed {full_path}")

# Replace 'figures' with the path to your directory
convert_png_to_jpeg('static/images/test')
