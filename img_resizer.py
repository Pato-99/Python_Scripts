import os
from PIL import Image

dir_path = input('Umístění složky: ')
os.chdir(dir_path)
print('Soubory ve složce: ')
for f in os.listdir():
    print(f)

print()
basewidth = int(input('Požadovaná šířka v pixelech: '))
print()

for f in os.listdir():
    print(f)
    
    img = Image.open(f)
    print(img.format, img.size, img.mode)

    f_name, f_ext = os.path.splitext(f)
    
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize))

    print('new size: '+str(img.size))

    img.save('{}x{} {}{}'.format(str(img.size[0]), str(img.size[1]), f_name, f_ext))
    img.close()

    print()