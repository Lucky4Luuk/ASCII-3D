import math
import random

DEPTHMAP = {3:"-",
            2:">",
            1:"V",
            0:"X"}

def render_cube_ascii(vx,vy,vz, rx,ry,rz) :
    pointlist = []

    rotx = math.radians(rx)
    roty = math.radians(ry)
    rotz = math.radians(rz)

    for x in range(vx) :
        for y in range(vy) :
            for z in range(vz) :
                dx = (32-vx)/2
                dy = (32-vy)/2
                dz = (32-vz)/2
                
                fx = x-16+dx
                fy = y-16+dy
                fz = z-16+dz

                resx = math.cos(roty)*fx - math.sin(roty)*fz
                resy = fy//2
                resz = math.cos(roty)*fz + math.sin(roty)*fx
                
                pointlist.append([resx,resy,resz])

    rpixels = []

    for p in pointlist :
        x = p[0]
        y = p[1]
        z = p[2]/50 + 1
        
        sx = round(x/z + 32)
        sy = round(y/z + 32)

        if sx > 63 or sy > 63 or sx < 0 or sy < 0 :
            print(sx,sy)

        d = int(p[2]/vz) * 4
        if d > 3 :
            print(sx,sy,d)
            d = 3

        rpixels.append([sx,sy,d])

    pixels = []
    for p in rpixels :
        if not p in pixels :
            pixels.append(p)

    screenchars = []
    for x in range(64) :
        screenchars.append([])
        for y in range(64) :
            screenchars[x].append(" ")

    for p in pixels :
        sx = p[0]
        sy = p[1]
        d = p[2]
        screenchars[sy][sx] = DEPTHMAP[d]

    msg = ""
    for row in screenchars :
        for char in row :
            msg = msg + char
        msg = msg + "\n"

    return msg

print(render_cube_ascii(16,16,16,0,45,0))
