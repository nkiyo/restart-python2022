# ref => https://qiita.com/baby-degu/items/674a09d9fc6b6cd73ce3
full_name = "Kiyoshi Nakahara"
chars = [c for c in full_name]
#print(chars)

matrix = [[2, 1, 5], [5, 99, 0], [33, 2, 4]]
row_max = [max(a) for a in matrix]
#print(row_max)

genius = ["Yang", "Tom", "Jerry", "Jack", "tom", "yang"]
l1 = [name for name in genius if name.startswith('Y')]
l2 = [name for name in genius if name.startswith('Y') or len(name) < 4]
l3 = [name for name in genius if len(name) < 4 and name.islower()]
print(l1, l2, l3)

genius2 = ["Jerry", "jack", "tom", "Yang"]
l4 = [name.capitalize() for name in genius2]
print(l4)

l5 = [name if name.startswith('Y') else 'Not genius' for name in genius2]
print(l5)

l6 = [char for name in genius2 if len(name) < 4 for char in name]
print(l6)


# ref => https://qiita.com/KTakahiro1729/items/c9cb757473de50652374
code = 'EBNO CSBU GJHVSJOH JU PVU TP RVJDLMZ'
d = {letter: code.count(letter) for letter in code}
print(f"{d}")


Mikado = ['Jimmu', 'Suizei', 'Annei', 'Itoku']
print(['{0}: {1}'.format(i + 1, Mikado[i]) for i in range(len(Mikado))])
print(['{0}: {1}'.format(i + 1, v) for i, v in enumerate(Mikado)])
