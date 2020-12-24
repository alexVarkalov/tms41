# Создать список учеников подобной структуры.
# Определить средний балл оценок по всем предметам,
# и вывести сведения о студентах, средний балл которых больше 4. [02-7.3-BL-02]

pupils = [
  {
        'firstname': 'Masha',
        'group': 'Ivanova',
        'physics': 7,
        'informatics': 6,
        'history': 8,
  },
  {
        'firstname': 'Sasha',
        'group': 'Petrova',
        'physics': 7,
        'informatics': 6,
        'history': 8,
  },
  {
        'firstname': 'Grisha',
        'group': 'Pavlov',
        'physics': 3,
        'informatics': 3,
        'history': 4,
  },
]

summ_phy = 0
summ_inf = 0
summ_his = 0

good_pupils = []

for pupil in pupils:
    summ_phy += pupil['physics']
    summ_inf += pupil['informatics']
    summ_his += pupil['history']
    if (pupil['physics'] + pupil['informatics'] + pupil['history']) / 3 > 4:
        good_pupils.append(pupil)

for pupil in good_pupils:
    print(f'{pupil["firstname"]} is good')
print()

amount_of_pupils = len(pupils)
mean_phy = summ_phy / amount_of_pupils
mean_inf = summ_inf / amount_of_pupils
mean_his = summ_his / amount_of_pupils

print(f'mean for physics is {mean_phy}')
print(f'mean for informatics is {mean_inf}')
print(f'mean for history {mean_his}')
