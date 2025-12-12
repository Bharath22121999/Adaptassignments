import os
import glob

# Settings
output_file = 'pytorch_model.bin'
part_pattern = 'pytorch_model.bin.part*'

# Find all parts and sort them to ensure correct order (part0, part1...)
parts = sorted(glob.glob(part_pattern))

if not parts:
    print("No part files found!")
else:
    print(f"Found {len(parts)} parts. Joining...")
    
    with open(output_file, 'wb') as outfile:
        for part in parts:
            print(f"Processing {part}...")
            with open(part, 'rb') as infile:
                outfile.write(infile.read())
    
    print(f"Success! {output_file} has been recreated.")
