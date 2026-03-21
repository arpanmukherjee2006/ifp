import os
import glob

# Files we already fixed or should not touch
SKIP_FILES = ["index.html", "research.html", "genetics.html", "tree-improvement.html"]

directory = "/home/abhishek/Pictures/ifp-main (4)/ifp-main"
# Recursively find all HTML files
html_files = glob.glob(os.path.join(directory, "**", "*.html"), recursive=True)

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
        duplicate_marker_idx = content.find('// Mobile dropdown toggle function', footer_idx)
        
        if duplicate_marker_idx != -1:
            end_idx = footer_idx + len('    </footer>')
            valid_content = content[:end_idx]
            
            # Determine if Flowbite is needed by checking if it's in the <head>
            needs_flowbite = "flowbite.min.css" in valid_content
            
            script = ""
            if needs_flowbite:
                script += '\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.2.1/flowbite.min.js"></script>'
            
            # Subdirectory files might need different paths for loader.js, 
            # let's assume they use "../components/loader.js" if they are in a subdirectory
            # Calculate relative depth
            rel_path = os.path.relpath(filepath, directory)
            depth = len(rel_path.split(os.sep)) - 1
            
            loader_prefix = "../" * depth
            loader_path = f"{loader_prefix}components/loader.js"
            
            script += f'\n    <script src="{loader_path}"></script>\n</body>\n</html>'
            
            new_content = valid_content + script
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
                
            print(f"Fixed recursively: {rel_path}")
            fixed_count += 1

print(f"Total files fixed in subdirectories: {fixed_count}")
