"""
Main entry point for make.fun news-image-20261119.
Copies the generated image to the output directory.
"""
import os
import shutil
import sys

def main():
    source = os.path.join(os.path.dirname(__file__), "entry.png")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(output_dir, "entry.png")
    
    if not os.path.exists(source):
        print(f"Error: {source} not found.")
        sys.exit(1)
    
    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, target)
    print(f"Success: {target} written.")

if __name__ == "__main__":
    main()
