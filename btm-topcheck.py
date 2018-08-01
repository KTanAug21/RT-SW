def bottom(grid,row, col):
	data = []
	kababayan = 0
	neighbors = 0
	agent = grid[row][col]
	#check bottom neighbors
	r = row+1                  
	if(row!=len(grid)-1):        
		start = col-1
		end = col+1

		#do not check respective corner side if element at a corner
		if(col==0):
			start = col
		elif(col==len(grid[0])-2):       # -2 for starting at 0 and for the \n after every line
			end = col
			
		#bottom neighbor walkthrough
		for c in range(start,end+1):
			neighbors +=1
			if(agent==grid[r][c]):
				kababayan +=1
			#end agent comparison
		#end bottom neighbor walkthrough
	#end bottom neighbor check 
	data.append(neighbors)
	data.append(kababayan)

	return data
#end bottom function

def top(grid,row, col):
	data = []
	kababayan = 0
	neighbors = 0
	agent = grid[row][col]
	#check top neighbors
	r = row-1                  
	if(row!=len(grid)-1):        
		start = col-1
		end = col+1
		#do not check respective corner side if element at a corner
		if(col==0):
			start = col
		elif(col==len(grid[0])-2):       # -2 for starting at 0 and for the \n after every line
			end = col
		
			
		#bottom neighbor walkthrough
		for c in range(start,end+1):
			neighbors +=1
			if(agent==grid[r][c]):
				kababayan +=1
			#end agent comparison
		#end bottom neighbor walkthrough
	#end bottom neighbor check 
	data.append(neighbors)
	data.append(kababayan)

	return data
#end bottom function