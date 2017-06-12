import math
import random

def rotate_data_y(data,r) :
    rot = math.radians(r)
    
    for x in range(len(data)) :
        layer = data[x]
        for y in range(len(layer)) :
            row = layer[y]
            for z in range(len(row)) :
                p = row[z]
                nx = math.cos(rot)*p[0] - math.sin(rot)*p[2]
                ny = y
                nz = math.cos(rot)*p[2] + math.sin(rot)*p[0]

                data[x][y][z] = [nx,ny,nz]

    return data

def render_cube_ascii(x,y,z) :
    data = []
    for layer in range(5) :
        data.append([])
        for row in range(5) :
            data[layer].append([])
            for point in range(5) :
                data[layer][row].append([layer,row,point])

    data = rotate_data(data,x,y,z)

    drawlist = []

    for layer in data :
        for row in layer :
            for p in row :
                dtc = math.sqrt(p[0]*p[0] + p[1]*p[1] + p[2]*p[2])
                point = p
                point.append(dtc)
                drawlist.append(point)

    drawlist = sorted(drawlist,key=lambda dtc: dtc[3],reverse=True)
