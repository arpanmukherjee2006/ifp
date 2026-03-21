import os

file_path = "components/footer.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace text 1
target1 = "Our vision at IFP is to develop and disseminate technological interventions for augmented eco-restoration, fragile forest ecosystem conservation, forest productivity enhancement, climate resilient agroforestry, rural life quality improvement and ethnoecological applications."
replacement1 = "The Government of Mysore had set up a Forest Research Laboratory (FRL) at Bangalore in 1988. In the initial years, work was carried out mainly on properties and uses of different timber species."
content = content.replace(target1, replacement1)

# Replace target 2 (iframe src)
target2 = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3662.8476682106584!2d85.24588880000002!3d23.3575328!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39f4dfb53e27ae7b%3A0xde6c2a0f4354386b!2sINSTITUTE%20OF%20FOREST%20PRODUCTITVITY!5e0!3m2!1sen!2sin!4v1770911487305!5m2!1sen!2sin"
replacement2 = "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d14651.390650756073!2d85.245889!3d23.357533!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39f4dfb53e27ae7b%3A0xde6c2a0f4354386b!2sINSTITUTE%20OF%20FOREST%20PRODUCTITVITY!5e0!3m2!1sen!2sin!4v1774073318663!5m2!1sen!2sin"
content = content.replace(target2, replacement2)

# Replace text 3
target3 = "© All Rights Reserved 2026 |vICFRE - Institute of Forest Productivity, Ranchi2026"
replacement3 = "© All Rights Reserved 2023 | Last updated Thursday 22 January 2026"
content = content.replace(target3, replacement3)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
