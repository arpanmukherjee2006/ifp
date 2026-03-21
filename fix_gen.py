import os

filepath = "/home/abhishek/Pictures/ifp-main (4)/ifp-main/genetics.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

footer_idx = content.find('    </footer>')

if footer_idx != -1:
    end_idx = footer_idx + len('    </footer>')
    valid_content = content[:end_idx]
    
    script = """
    <script src="components/loader.js"></script>
</body>
</html>"""
    
    new_content = valid_content + "\n" + script
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Fixed genetics.html")
else:
    print("Could not find footer closing tag in genetics.html")
