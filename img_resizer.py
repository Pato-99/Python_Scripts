import os
from PIL import Image

print("""
------------------------------------------
        Měnič rozlišení fotek
------------------------------------------""")

print("""
Vyberte kvalitu exportu:
 
    1 - 75 %
    2 - 50 %
    3 - 25 %
    """)


exports = [0.75, 0.5, 0.25]
exts = ['.jpg', '.png', '.jpeg']

selection = int(input()) - 1

cwd = os.getcwd()
os.mkdir('export')

for f in os.listdir():

    if os.path.splitext(f)[1].lower() not in exts:
        continue

    with Image.open(f) as img:
        img = img.resize((int(img.size[0] * exports[selection]),   # resizes the image
                          int(img.size[1] * exports[selection])))

        f_name, f_ext = os.path.splitext(f)

        os.chdir('export')
        img.save('{}_{}x{}{}'.format(f_name, str(img.size[0]), str(img.size[1]), f_ext))  # saves the image
        os.chdir(cwd)

input('Hotovo')
