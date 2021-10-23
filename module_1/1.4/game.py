def game(terra, power):
    sm = power
    for t_lst in terra:
        for t in t_lst:
            if t <= sm:
                sm += t
            else: break
    return sm


lst = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
print( game(lst, 1) )
print( game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1) )
