#!/usr/bin/env python3
"""
Batch Image Conversion Script for Hugo Sites
Converts images in assets/media, content, and static/images to multiple formats
"""

import os
import sys
from pathlib import Path
from PIL import Image
import pillow_avif  # pip install pillow-avif-plugin

def convert_image(input_path, output_dir, formats=['jpg', 'webp', 'avif']):
    """Convert a single image to multiple formats"""
    try:
        with Image.open(input_path) as img:
            # Convert RGBA to RGB for formats that don't support transparency
            if img.mode in ('RGBA', 'LA', 'P'):
                if 'png' not in formats:
                    # Create white background for non-PNG formats
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = background
                else:
                    img = img.convert('RGBA')
            
            base_name = Path(input_path).stem
            
            for fmt in formats:
                if fmt == 'jpg':
                    output_path = output_dir / f"{base_name}.jpg"
                    img_to_save = img.convert('RGB') if img.mode != 'RGB' else img
                    img_to_save.save(output_path, 'JPEG', quality=85, optimize=True)
                    
                elif fmt == 'webp':
                    output_path = output_dir / f"{base_name}.webp"
                    img.save(output_path, 'WEBP', quality=85, method=6)
                    
                elif fmt == 'avif':
                    output_path = output_dir / f"{base_name}.avif"
                    img.save(output_path, 'AVIF', quality=75, speed=6)
                    
                elif fmt == 'png':
                    output_path = output_dir / f"{base_name}.png"
                    img.save(output_path, 'PNG', optimize=True)
            
            print(f"✓ Converted: {input_path}")
            
    except Exception as e:
        print(f"✗ Failed to convert {input_path}: {e}")

def process_directory(directory, formats=['jpg', 'webp', 'avif']):
    """Process all images in a directory recursively"""
    directory = Path(directory)
    if not directory.exists():
        print(f"Directory doesn't exist: {directory}")
        return
    
    supported_formats = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff', '.tif'}
    
    for root, dirs, files in os.walk(directory):
        root_path = Path(root)
        
        # Create output directory structure
        output_dir = root_path / "converted"
        output_dir.mkdir(exist_ok=True)
        
        for file in files:
            if Path(file).suffix.lower() in supported_formats:
                input_path = root_path / file
                
                # Skip if it's a GIF (preserve animation)
                if Path(file).suffix.lower() == '.gif':
                    continue
                    
                convert_image(input_path, output_dir, formats)

def main():
    """Main conversion process"""
    print("🖼️  Starting batch image conversion...")
    
    # Directories to process
    directories = [
        "assets/media",
        "content",
        "static/images"
    ]
    
    # Formats to generate
    formats = ['jpg', 'webp', 'avif']
    
    for directory in directories:
        if os.path.exists(directory):
            print(f"\n📁 Processing: {directory}")
            process_directory(directory, formats)
        else:
            print(f"📁 Skipping (doesn't exist): {directory}")
    
    print("\n✅ Conversion complete!")

if __name__ == "__main__":
    main()
