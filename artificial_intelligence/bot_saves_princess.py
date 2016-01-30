#!/bin/python

# unoptimized


def displayPathtoPrincess(n,grid):
    list_grid = []
    for i in grid:
        list_grid.append(list(i))
      
    for i in xrange(len(list_grid)):
        for j in xrange(len(list_grid[i])):
            if list_grid[i][j] == 'p':
                p_x = j
                p_y = i
            elif list_grid[i][j] == 'm':
                m_x = j
                m_y = i
    
    if m_x - p_x < 0:
        for a in range(0, abs(m_x - p_x)):
            print 'RIGHT'
    elif m_x - p_x > 0:
        for b in range(0, abs(m_x - p_x)):
            print 'LEFT'
                        
    if m_y - p_y < 0:
        for c in range(0, abs(m_y - p_y)):
            print 'DOWN'
    elif m_y - p_y > 0:
        for d in range(0, abs(m_y - p_y)):
            print 'UP'                    
     
    return n, grid

#print all the moves here
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
