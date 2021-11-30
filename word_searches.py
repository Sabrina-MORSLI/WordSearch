from copy import deepcopy
# Open files and format data from: words.dic, grid

# hidden_words = open("words.dic").read().splitlines()

# my_list = open("grid").read().splitlines()
# i = 0
# grid = []
# for elem in my_list:
#     elem = my_list[i:i+1]
#     i = i + 1
#     grid.append(elem)

hgrid = deepcopy(grid)
found_hwords = []
counter = 1

# print("\n***HORIZONTAL MATCHES***\n")

for x in range(len(hidden_words)):
    for y in range(len(hgrid)):
        if hidden_words[x] in grid[y][0]:

            found_hwords.append(hidden_words[x])
            counter = counter + 1
            
        if hidden_words[x][::-1] in grid[y][0]:

            found_hwords.append(hidden_words[x])
            counter = counter + 1

           

# print("found_hwords (horizontal matches) =",found_hwords)
hidden_words = [e for e in hidden_words if e not in found_hwords]
# print("hidden_words (after horizontal matches removed) =", hidden_words,"\n")

# vertical search downward & upward

# print("\n***VERTICAL MATCHES***\n")

vertical_grid = []
for i in range(len(grid[0][0])):
    vertical_grid.append([])
    for j in range(len(grid)):
        vertical_grid[i].append(grid[j][0][i])
        vertical_grid[i] = [''.join(vertical_grid[i])]


vgrid = deepcopy(vertical_grid)

found_vwords = []
for x in range(len(hidden_words)):
    for y in range(len(vertical_grid)):
        if hidden_words[x] in vertical_grid[y][0]:
            found_vwords.append(hidden_words[x])
            
            
        if hidden_words[x][::-1] in vertical_grid[y][0]:
            found_vwords.append(hidden_words[x])
            

# print("found_words (vertical matches) =",found_vwords)
hidden_words = [e for e in hidden_words if e not in found_vwords]
# print("hidden_words (after vertical matches removed) =", hidden_words,"\n")


# ***DIAGONALS***

# "↖ Diagonal NW (northwest, upper left) match: "
# "↗ Diagonal NE (northeast, upper right) match: "
# "↘ Diagonal SE (southeast, lower right) match: "
# "↙ Diagonal SW (southwest, lower left) match: "

# créer une liste avec lettres séparées
new_grid = []
for i in range(len(grid)):
    elem = grid[i][0]
    list_elem = list(elem)
    new_grid.append(list_elem)

# pour créer une grille de toutes les diagonales:

max_col = len(new_grid)
max_rows = len(new_grid[0])
se_diag = [[] for i in range(max_col + max_rows - 1)]
sw_diag = [[] for i in range(len(se_diag))]
min_sw_diag = -max_col + 1

for y in range(max_col):
    for x in range(max_rows):
        se_diag[x+y].append(new_grid[y][x])
        se_diag[x+y] = [''.join(se_diag[x+y])]
        sw_diag[-min_sw_diag+x-y].append(new_grid[y][x])
        sw_diag[-min_sw_diag+x-y] = [''.join(sw_diag[-min_sw_diag+x-y])]
# print("diagonales NW corner SW direction: ", se_diag)
# print("diagonales SW corner SE direction: ", sw_diag)

found_se_diag_words = []
for x in range(len(hidden_words)):
    for y in range(len(se_diag)):
        if hidden_words[x] in se_diag[y][0]:

            found_se_diag_words.append(hidden_words[x])

hidden_words = [e for e in hidden_words if e not in found_se_diag_words]


for x in range(len(hidden_words)):
    for y in range(len(se_diag)):
        if hidden_words[x][::-1] in se_diag[y][0]:

            found_se_diag_words.append(hidden_words[x])

hidden_words = [e for e in hidden_words if e not in found_se_diag_words]


found_sw_diag_words = []
for x in range(len(hidden_words)):
    for y in range(len(sw_diag)):
        if hidden_words[x] in sw_diag[y][0]:

            found_sw_diag_words.append(hidden_words[x])

hidden_words = [e for e in hidden_words if e not in found_sw_diag_words]


for x in range(len(hidden_words)):
    for y in range(len(sw_diag)):
        if hidden_words[x][::-1] in sw_diag[y][0]:

            found_sw_diag_words.append(hidden_words[x])

hidden_words = [e for e in hidden_words if e not in found_sw_diag_words]

print(hidden_words)
