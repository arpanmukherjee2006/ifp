import os
import glob

# Files we already fixed or should not touch
SKIP_FILES = ["index.html", "research.html", "genetics.html", "tree-improvement.html"]

directory = "/home/abhishek/Pictures/ifp-main (4)/ifp-main"
html_files = glob.glob(os.path.join(directory, "*.html"))

fixed_count = 0

for filepath in html_files:
    filename = os.path.basename(filepath)
    if filename in SKIP_FILES:
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # The duplicated content always starts shortly after the first </footer>
    footer_idx = content.find('    </footer>')

    if footer_idx != -1:
        # Check if there is duplication by looking for a second body tag or the mobile toggle script AFTER the footer
        # A simpler way is to find the index of the next "<body" or "<script>\n        // Mobile dropdown"
        duplicate_marker_idx = content.find('// Mobile dropdown toggle function', footer_idx)
        
        if duplicate_marker_idx != -1:
            end_idx = footer_idx + len('    </footer>')
            valid_content = content[:end_idx]
            
            # Determine if Flowbite is needed by checking if it's in the <head>
            needs_flowbite = "flowbite.min.css" in valid_content
            
            script = ""
            if needs_flowbite:
                script += '\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.2.1/flowbite.min.js"></script>'
                
            script += '\n    <script src="components/loader.js"></script>\n</body>\n</html>'
            
            new_content = valid_content + script
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
                
            print(f"Fixed: {filename}")
            fixed_count += 1
        else:
            print(f"No duplicate found in: {filename}")
    else:
        print(f"Skipped {filename}: No footer tag found.")

print(f"Total files fixed: {fixed_count}")
