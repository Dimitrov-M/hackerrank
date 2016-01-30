#!/usr/bin/python
def next_move(posr, posc, board):
    bot = [posr, posc]
    list_grid = []
    for i in board:
        list_grid.append(list(i))
    
    dirty = []
    for i in xrange(len(list_grid)):
        for j in xrange(len(list_grid[i])):
            if list_grid[i][j] == 'd':
                dirty.append([i,j])
               
    nearest = dirty[0]            
    for i in range(0, len(dirty)):
        if abs(bot[0] - dirty[i][0]) + abs(bot[1] - dirty[i][1]) < abs(nearest[0] - dirty[i][0]) + abs(nearest[1] - dirty[i][1]):
            nearest = dirty[i]
        
    if bot[1] - nearest[1] < 0:
        print 'RIGHT'
    elif bot[1] - nearest[1] > 0:
        print 'LEFT'
    elif bot[0] - nearest[0] < 0:
        print 'DOWN'
    elif bot[0] - nearest[0] > 0:
        print 'UP'
    else:
        print 'CLEAN'
     
    
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)