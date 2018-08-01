from decimal import Decimal
#PROBLEM SET FUNCTIONS######################################################################
def loadgrid(filename):
	#variable declaration
	grid_array = []             #append new arrays here

	#read file
	file = open(filename, "r");

	#store each line characters into an array that will be stored in an array of arrays: grid_array
	for line in file:
		#recreate empty list for each line
		line_array = []
		for char in line:
			line_array.append(char.rstrip('\n'))
		#end cahracters in line list
		grid_array.append(line_array)
	#end lines list

	return grid_array
#end load_grid

def dissimilarity(grid,row1,col1,row2, col2):
	total_x, total_y, sub_x, sub_y = 0,0,0,0
	
	#tally all Xs and Os in entire grid
	tally_all = tally(grid)                         #array of tallied values of x and o for te entire region
	total_x = tally_all[0]
	total_y = tally_all[1]

	#tally sub_region's Xs and Os
	sub_region = sub_grid(grid,row1,col1,row2,col2)  #get sub grid
	tally_region = tally(sub_region)                 #array of tallied values of x and o for sub grid
	sub_x = tally_region[0]													 
	sub_y = tally_region[1]

	#compute for the dissimilarity of the subregion
	dissimilarity = round(0.5* abs((float(sub_x)/total_x) - float(float(sub_y)/total_y)),3)

	return dissimilarity
#end dissimilarity



#SUB FUNCTIONS#########################################################################
def tally(grid):
	tally = []
	total_x, total_y =0,0

	for line in grid:
		for char in line:
			if(char=='X'):
				total_x +=1
			elif(char=='O'):
				total_y +=1
		#end character walkthrough
	#end line walkthrough

	tally.append(total_x)
	tally.append(total_y)

	return tally
#end tally function

def sub_grid(grid, row1,col1,row2,col2):
	sub_region = []

	#get hold of subregion of grid   
	if(col1<col2):#col1 left, col2 right
		if(row1<row2):#row1 top, row2 bottom
			for r in range(row1,row2+1):
				new = []
				for c in range(col1,col2+1):
					new.append(grid[r][c])
				#end 
				sub_region.append(new)
			#end 

		elif(row1>row2):#row2 top, row1 bottom
			for r in range(row2,row1+1):
				new = []
				for c in range(col1,col2+1):
					new.append(grid[r][c])
				#end 
				sub_region.append(new)
			#end 
		else:#both rows the same
			new = []
			r = row1;
			for c in range(col1,col2+1):
				new.append(grid[r][c])
			#end
			sub_region.append(new)
	elif(col1>col2):#col2 left, col1 right
		if(row1<row2):#row1 top, row2 bottom
			for r in range(row1,row2+1):
				new = []
				for c in range(col2,col1+1):
					new.append(grid[r][c])
				#end 
				sub_region.append(new)
			#end 

		elif(row1>row2):#row2 top, row1 bottom
			for r in range(row2,row1+1):
				new = []
				for c in range(col2,col1+1):
					new.append(grid[r][c])
				#end 
				sub_region.append(new)
			#end 
		else:#both rows the same
			new = []
			r = row1;
			for c in range(col2,col1+1):
				new.append(grid[r][c])
			#end
			sub_region.append(new)
	else:#both are in the same column
		if(row1<row2):#row1 top, row2 bottom
			c = col1;
			new = []
			for r in range(row1,row2+1):
				new.append(grid[r][c])
				sub_region.append(new)
			#end  

		elif(row1>row2):#row2 top, row1 bottom
			for r in range(row2,row1+1):
				new = []
				new.append(grid[r][c])
				#end 
				sub_region.append(new)
			#end 
		else:#both rows the same
			sub_region.append(grid[row1][col1])
	#end comparison of both corners

	return sub_region
#end sub_region function
def kath(grid,t):

	for idr,line in enumerate(grid):
		for idc, char in enumerate(line):
			if(idc!=len(grid[0])-1):                 #dont include \n characters
				kababayan = 0
				neighbors = 0
				#TOP NEIGHBORS EVAL
				if(idr!=0):#element row is not top
					neighbors +=1                    #top neighbor exists         
					if(grid[idr-1][idc]==char):
						kababayan+=1                   #top neighbor kababayan
					if(idc!=0):
						neighbors+=1									#topleft exists
						if(grid[idr-1][idc-1]==char):
							kababayan+=1                 #topleft kababayan
					if(idc!=len(grid[0])-2):        # -2 for 0 index start and \n character
						neighbors+=1                  #topright exists
						if(grid[idr-1][idc+1]==char):
							kababayan+=1                #topright kababayan

				#BOTTOM NEIGHBORS EVAL
				if(idr!=len(grid)-1):#element row is not bottom
					neighbors +=1                    #btm neighbor exists         
					if(grid[idr+1][idc]==char):
						kababayan+=1                   #bt, neighbor kababayan
					if(idc!=0):
						neighbors+=1									#btmleft exists
						if(grid[idr+1][idc-1]==char):
							kababayan+=1                 #bt,left kababayan
					if(idc!=len(grid[0])-2):        # -2 for 0 index start and \n character
						neighbors+=1                  #btmright exists
						if(grid[idr+1][idc+1]==char):
							kababayan+=1                #btmright kababayan

				#SIDE NEIGHBORS
				if(idc!=0):
					neighbors+=1#left neighbor exists
					if(grid[idr][idc-1]==char):
						kababayan +=1
				if(idc!=len(grid[0])-2):
					neighbors+=1
					if(grid[idr][idc+1]==char):
						kababayan+=1

				result = float(kababayan)/float(neighbors)
				#print(str(idr)+"," +str(idc) + ": "+str(result)+" from: "+str(kababayan)+"/"+str(neighbors))
				if(result < t):
					grid[idr][idc] = ''
	return grid
				







#test 
k = loadgrid("file.txt")
d = dissimilarity(k, 0,6,3,9)
grid = kath(k,0.5)

print(k)
