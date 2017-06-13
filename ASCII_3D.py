import math
import random

def rotate_data_y(data,r) :
    rot = math.radians(r)
    
    for p in range(len(data)) :
        po = data[p]
        
        nx = math.cos(rot)*po[0] - math.sin(rot)*po[2]
        ny = po[1]
        nz = math.cos(rot)*po[2] + math.sin(rot)*po[0]

        data[p] = [nx,ny,nz]

    return data

def transform_data(data,tx,ty,tz) :
    for p in range(len(data)) :
        po = data[p]
        data[p] = [po[0]-tx,po[1]-ty,po[2]-tz]

    return data

def old_render_cube_ascii(x,y,z) :
    data = []
    for x in range(16) :
        for y in range(16) :
            for z in range(16) :
                data.append([x-8,y-8,z-8])

    data = rotate_data_y(data,y)

    data = transform_data(data,0,0,18)

    drawlist = []

    for po in range(len(data)) :
        p = data[po]
        dtc = math.sqrt(p[0]*p[0] + p[1]*p[1] + p[2]*p[2])
        point = p
        point.append(dtc)
        drawlist.append(point)

    drawlist = sorted(drawlist,key=lambda dtc: dtc[3],reverse=True)

    screendata = []

    for x in range(64) :
        screendata.append([])
        for y in range(64) :
            screendata[x].append(" ")

    for p in drawlist :
        x = p[0]/2
        y = p[1]/4
        z = p[2]/25

        if z == 0 :
            z = 0.001
        
        sx = int(x/z + 32)//2
        sy = int(y/z + 32)//2

        if sx > -1 and sx < 64 :
            if sy > -1 and sy < 64 :
                screendata[sx][sy] = "@"
        else :
            print(sx,sy)

    msg = ""
    
    for row in screendata :
        for char in row :
            msg = msg + str(char)
        msg = msg + "\n"

    print(msg)

def render_cube_ascii(x,y,z) :
    data = []
    for x in range(32) :
        data.append([])
        for y in range(32) :
            data[x].append([])
            for z in range(128) :
                data[x][y].append(0)

    for x in range(8,24) :
        for y in range(8,24) :
            for z in range(8,24) :
                data[x][y][z] = 1

    #data = rotate_data_y(data,y)

    #data = transform_data(data,0,0,18)

    charlist = []
    for x in range(65) :
        charlist.append([])
        for y in range(65) :
            charlist[x].append(" ")

    for x in range(65) :
        for y in range(65) :
            for z in range(128) :
                nz = int(z*5)
                wx = int(((x - 32.5) * nz)/5)
                wy = int(((y - 32.5) * nz)/5)
                wz = nz

                if z > 0 :
                    try :
                        if data[wx][wy][wz] == 1 :
                            charlist[x][y] = "@"
                            break
                    except Exception :
                        #print(wx,wy,wz)
                        pass

    msg = ""

    for row in charlist :
        for char in row :
            msg = msg + char
        msg = msg + "\n"

    print(msg)

def poly_render_cube_ascii(x,y,z) :
    verts = [[-1,-1,-1],
             [ 1,-1,-1],
             [ 1,-1, 1],
             [-1,-1, 1],

             [-1, 1,-1],
             [ 1, 1,-1],
             [ 1, 1, 1],
             [-1, 1, 1]]

    faces = [[0,2,1],
             [0,2,3],
             
             [4,6,5],
             [4,6,7],

             [0,5,4],
             [0,1,4]]

    charlist = []

    for x in range(64) :
        charlist.append([])
        for y in range(64) :
            charlist[x].append(" ")

    for f in faces :
        v1 = verts[f[0]]
        v2 = verts[f[1]]
        v3 = verts[f[2]]

        sx1 = int(v1[0]/v1[2]) + 32
        sy1 = int(v1[1]/v1[2]) + 32

        sx2 = int(v2[0]/v2[2]) + 32
        sy2 = int(v2[1]/v2[2]) + 32

        sx3 = int(v3[0]/v3[2]) + 32
        sy3 = int(v3[1]/v3[2]) + 32

        for px in range(64) :
            for py in range(64) :
                area = 0.5 *(-sy2*sx3 + sy1*(-sx2 + sx3) + sx1*(sy2 - sy3) + sx2*sy3)

                s = 1/(2*area)*(sy1*sx3 - sx1*sy3 + (sy3 - sy1)*px + (sx1 - sx3)*py)
                t = 1/(2*area)*(sx1*sy2 - sy1*sx2 + (sy1 - sy2)*px + (sx2 - sx1)*py)

                if s > 0 and t > 0 and 1-s-t > 0 :
                    charlist[px][py] = "@"

    msg = ""

    for row in charlist :
        for char in row :
            msg = msg + char
        msg = msg + "\n"

    print(msg)

render_cube_ascii(0,0,0)
