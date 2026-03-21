import os
import re

filepath = "/home/abhishek/Pictures/ifp-main (4)/ifp-main/research.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# We know the valid content ends at the footer closing tag:
#    </footer>
footer_idx = content.find('    </footer>')

if footer_idx != -1:
    end_idx = footer_idx + len('    </footer>')
    valid_content = content[:end_idx]
    
    # We need to append loader.js and the scientist blur script, then </body></html>
    scientist_script = """
    <script src="components/loader.js"></script>
    <script>
        // Scientist Section Progressive Scroll Blur Animation
        const scientistSection = document.getElementById('scientist-section');
        const scientistBg = document.getElementById('scientist-bg');
        const scientistOverlay = document.getElementById('scientist-overlay');
        const scientistContent = document.getElementById('scientist-content');

        function updateScientistBlur() {
            if (!scientistSection || !scientistBg || !scientistOverlay || !scientistContent) return;

            const rect = scientistSection.getBoundingClientRect();
            const windowHeight = window.innerHeight;

            const sectionTop = rect.top;
            const sectionHeight = rect.height;

            let scrollProgress = 0;

            if (sectionTop < windowHeight && sectionTop + sectionHeight > 0) {
                scrollProgress = Math.max(0, Math.min(1, (windowHeight - sectionTop) / (windowHeight + sectionHeight / 2)));
            }

            const blurAmount = scrollProgress * 15;
            const overlayOpacity = 0.3 + (scrollProgress * 0.40);
            const contentOpacity = Math.max(0.3, scrollProgress);

            scientistBg.style.filter = `blur(${blurAmount}px)`;
            scientistOverlay.style.backgroundColor = `rgba(0, 0, 0, ${overlayOpacity})`;
            scientistContent.style.opacity = contentOpacity;
            scientistContent.style.transform = `translateY(${(1 - scrollProgress) * 20}px)`;
        }

        window.addEventListener('scroll', updateScientistBlur);
        document.addEventListener('DOMContentLoaded', updateScientistBlur);
        updateScientistBlur();
    </script>
</body>
</html>"""
    
    new_content = valid_content + "\n" + scientist_script
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Fixed research.html")
else:
    print("Could not find footer closing tag in research.html")
