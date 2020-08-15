import os

dir_path = input('Umístění složky: ')
os.chdir(dir_path)
print('Soubory ve složce:')
for f in os.listdir():
    print(f)

print()
title = input('Nový název: ')
pripony = input('Přípony(oddělujte mezerou): ')
list_pripon = pripony.split(' ')
print('Přípony ke zpracování:')
print(list_pripon)

#print(os.getcwd())
#print(os.listdir())

print()
zachovat_cislovani = input('Zachovat původní číslování?(a/n)')
if zachovat_cislovani == 'n':
    print()
    print('Formáty nového číslování')
    print('1) - 1, 2, 3...')
    print('2) - 01, 02, 03...')
    print('3) - 001, 002, 003...')
    volba = input('Volba(1/2/3): ')

    i = 1
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        if f_ext in list_pripon:
            f_num = str(i).zfill(int(volba))
    
            new_name = '{}_{}{}'.format(title, f_num, f_ext)
            print(new_name)
        
            os.rename(f, new_name)
            i += 1
        else:
            pass
            i += 1

elif zachovat_cislovani == 'a':
    oddelovac = input('Sem napište znak, který odděluje číslování od názvu: ')
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        if f_ext in list_pripon:
            f_title, f_num = f_name.split(oddelovac)

            new_name = '{}{}{}{}'.format(title, oddelovac, f_num, f_ext)
            print(new_name)
            
            os.rename(f, new_name)
        else:
            pass
        
else:
    print('error')

print('Soubory byly přejmenovány.')
input('Pro ukončení stiskněte Enter.')