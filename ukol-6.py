with open('znamky.txt', encoding='utf-8') as file:
    radky = file.readlines()

radky_first = radky[1:]
radek_zero = radky[0]

new_radky = [radky_first.replace('1', 'A').replace ('2', 'B').replace ('3', 'C').replace ('4', 'D').replace ('5', 'F')  for radky_first in radky_first]
radky_all_together  = [radek_zero] + new_radky


print (radky_all_together)


with open('znamky_final.txt', mode='w', encoding='utf-8') as vystup:
    vystup.writelines(radky_all_together)


