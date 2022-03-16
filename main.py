import itertools

medidas = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]

combinations = list(itertools.combinations_with_replacement([300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900], 2))

for a, b in combinations:
    print(f'{a}\t{b}')

