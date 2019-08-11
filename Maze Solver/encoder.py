import sys
import numpy as np

gridfile = sys.argv[1]
p = eval(sys.argv[2])
f = open(gridfile,"r")

grid = np.array([[eval(el) for el in line.split()] for line in f.readlines()])

actions = 4
states = np.count_nonzero(grid - 1)
disc = 1
transition = []
start = -1
end = []

grid_to_state = {}
state_to_grid = {}

count = 0
for i in range(grid.shape[0]) :
	for j in range(grid.shape[1]) :
		if grid[i][j] == 2 :
			start = count
		if grid[i][j] == 3 :
			end.append(count)
		if grid[i][j] != 1 :
			grid_to_state[(i,j)] = count
			state_to_grid[count] = (i,j)
			count += 1

for i in range(grid.shape[0]) :
	for j in range(grid.shape[1]) :
		if grid[i][j] in [0,2,3] :
			s1 = grid_to_state[(i,j)]
			s2 = []
			action = []
			if i > 0 and grid[i-1][j] != 1 :
				s2.append(grid_to_state[(i-1,j)])
				action.append(0)
			if i < grid.shape[0]-1 and grid[i+1][j] != 1 :
				s2.append(grid_to_state[(i+1,j)])
				action.append(1)
			if j > 0 and grid[i][j-1] != 1 :
				s2.append(grid_to_state[(i,j-1)])
				action.append(3)
			if j < grid.shape[1]-1 and grid[i][j+1] != 1 :
				s2.append(grid_to_state[(i,j+1)])
				action.append(2)

			correct_prob = p + ((1-p)*1.0)/len(s2)
			wrong_prob = ((1-p)*1.0)/len(s2)
			for t in range(len(s2)) :
				if s2[t] in end :
					transition.append([s1,action[t],s2[t],100,correct_prob])
				else :
					transition.append([s1,action[t],s2[t],0,correct_prob])

				for k in range(len(s2)) :
					if k != t : 
						if s2[k] in end :
							transition.append([s1,action[t],s2[k],100,wrong_prob])
						else :
							transition.append([s1,action[t],s2[k],0,wrong_prob])

			

disc = 0.9

print("numStates",states)
print("numActions",actions)
print("start",start)
print("end",*end)
for el in transition :
	print("transition",*el)
print("discount",disc)


