import pygame

width = 800
height = 800

def move(v, ship, wp):
    mv = tuple(v * e for e in wp)
    return tuple(map(sum, zip(ship, mv)))


def rwp(wp, v):
    x, y = wp
    v %= 360
    if v == 90:
        return y, x * -1
    elif v == 180:
        return x * -1, y * -1
    elif v == 270:
        return y * -1, x
    else:
        return x, y


def cycle(data, actor, waypoint):
    ship_p = []
    waypoint_p = []
    acts = {
        "E": lambda x, p: (p[0] + x, p[1]),
        "W": lambda x, p: (p[0] - x, p[1]),
        "S": lambda x, p: (p[0], p[1] - x),
        "N": lambda x, p: (p[0], p[1] + x),
    }

    mvrs = [(0,0), waypoint] # ship and wp
    for line in data:
        ship_p.append(mvrs[0])
        waypoint_p.append(mvrs[1])
        i = line[0]
        v = int(line[1:])
        if i == "F":
            mvrs[0] = move(v, *mvrs)
        elif i in "RL":
            if i == "L":
                v = v * -1
            mvrs[1] = rwp(mvrs[1], v)
        else:
            mvrs[actor] = acts[i](v, mvrs[actor])
    return abs(mvrs[0][0]) + abs(mvrs[0][1]), ship_p, waypoint_p

def drawwps(wps, step, screen, scale):
    global width
    global height


    for i in range(1, step):
        px,py = wps[i-1]
        cx,cy = wps[i]
        px = (px*scale)+(width/2)
        py = (py*scale)+(height/2)
        cx = (cx*scale)+(width/2)
        cy = (cy*scale)+(height/2)
        pygame.draw.line(screen,(255,0,0),(px,py),(cx,cy))



def drawships(ships, wps, step, screen, sw, force=False, scalr=1):
    global width
    global height
    color = (34,80,149)
    minwidth = min([x[0] for x in ships[0:step]])
    maxwidth = max([x[0] for x in ships[0:step]])
    minheight = max([x[1] for x in ships[0:step]])
    maxheight = max([x[1] for x in ships[0:step]])
    maxwidth = max(abs(minwidth), maxwidth)
    maxheight = max(abs(minheight), maxheight)
    w_over = maxwidth - width/2
    h_over = maxheight - height/2
    p_over = max(w_over, h_over)
    if p_over > 0:
        scale = (width/2) / (abs(p_over)+width/2)
        scale *= 0.9
    else:
        # -200
        # 400/400
        # 2
        #
        scale = (width/2) / abs(p_over)
        scale = 1

    if force:
        scale = scalr

    for i in range(1, step):
        if sw == i:
            continue
        if i > sw:
            color = (221,1,0)
        px,py = ships[i-1]
        cx,cy = ships[i]
        px = (px*scale)+(width/2)
        py = (py*scale)+(height/2)
        cx = (cx*scale)+(width/2)
        cy = (cy*scale)+(height/2)
        pygame.draw.line(screen,color,(px,py),(cx,cy))
    if sw == step:

        wpx,wpy = wps[step-1]
        wpx = wpx*scale
        wpy = wpy*scale
        wpx += cx
        wpy += cy
        factor=5
        pygame.draw.rect(screen,(0,0,0),(wpx-((scale*factor)/2), wpy-((scale*factor)/2), scale*factor, scale*factor))
        #print("draw from {},{} to {},{}".format(px,py,cx,cy))
    return scale


def main():
    global width
    global height
    background_colour =(250,201,1)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Advent of Code')
    screen.fill(background_colour)
    pygame.display.flip()
    running = True

    with open('day12.txt', 'r') as f:
        data = f.readlines()
    p1, s1, w1 = cycle(data, 0, (1, 0))
    p2, s2, w2 = cycle(data, 1, (10, 1))
    sw = len(s1)
    ships = s1+s2
    wps = w1+w2
    step = 2
    scale = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if step<len(ships):
            screen.fill(background_colour)
            scale = drawships(ships, wps, min(step,len(ships)-1), screen, sw)
            step += 1
            pygame.display.flip()
            pygame.time.wait(5)
        else:
            screen.fill(background_colour)
            drawships(ships, wps, min(step,len(ships)-1), screen, sw, True, scale)
            scale += 0.001
            pygame.display.flip()
            pygame.time.wait(5)


if __name__ == "__main__":
    main()
