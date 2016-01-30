#!/bin/python
def nextMove(n,r,c,grid):
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
            return 'RIGHT'
    elif m_x - p_x > 0:
        for b in range(0, abs(m_x - p_x)):
            return 'LEFT'
                       
    if m_y - p_y < 0:
        for c in range(0, abs(m_y - p_y)):
            return 'DOWN'
    elif m_y - p_y > 0:
        for d in range(0, abs(m_y - p_y)):
            return 'UP'
            
n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)
