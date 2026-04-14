from PIL import Image
import os

input_folder = "image"
output_folder = "image"

for filename in os.listdir(input_folder):
    if filename.endswith(".webp"):
        webp_path = os.path.join(input_folder, filename)
        
        png_name = filename.replace(".webp", ".png")
        png_path = os.path.join(output_folder, png_name)

        img = Image.open(webp_path).convert("RGBA")
        img.save(png_path, "PNG")

        print(f"Converted: {filename} -> {png_name}")

print("✅ Дайын!")