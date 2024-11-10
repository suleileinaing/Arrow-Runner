#to make list of coordinate to create path 

text = input ("enter:" )

point = (0,550)
list = []
list.append(point)
for char in text:
    if char == 'j':
        new = (point[0]-50, point[1])
        list.append(point)
        point = new
    if char == 'k':
        new = (point[0], point[1]+50)
        list.append(point)
        point = new

    if char == 'l':
        new = (point[0]+50, point[1])
        list.append(point)
        point = new

    if char == 'i':
        new = (point[0], point[1]-50)
        list.append(point)
        point = new

print(list)