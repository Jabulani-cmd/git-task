def minesweeper(grid):
    if not grid:return[]
    rows,cols=len(grid),len(grid[0])
    result=[[0 for _ in range(cols)]for _ in range(rows)]
    directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]=='#':
                for di,dj in directions:
                    ni,nj=i+di,j+dj
                    if 0<=ni<rows and 0<=nj<cols:result[ni][nj]+=1
                result[i][j]='#'
    for i in range(rows):
        for j in range(cols):
            if result[i][j]!='#':result[i][j]=str(result[i][j])
    return resultpyth