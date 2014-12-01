'''
Paint fill
'''
# Fictional color matrix

color = [[1, 1, 1],
         [2, 2, 2],
         [2, 3, 2],
         [3, 3, 3]]

max_x = len(color) - 1
max_y = len(color) - 1

def paint_fill(x, y, ocolor, ncolor):

    if x < 0 or y < 0 or x >= max_x or y >= max_y:
        return False

    if color[x][y] == ocolor:
        color[x][y] = ncolor
        paint_fill(x-1, y, ocolor, ncolor)
        paint_fill(x+1, y, ocolor, ncolor)
        paint_fill(x, y+1, ocolor, ncolor)
        paint_fill(x, y-1, ocolor, ncolor)

    return True

paint_fill(1, 0, 2, 4)
print(color)
