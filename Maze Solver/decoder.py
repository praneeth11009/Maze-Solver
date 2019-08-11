import sys
import numpy as np

np.random.seed(0)

gridfile = sys.argv[1]
valuefile = sys.argv[2]
p = eval(sys.argv[3])
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
		if grid[i][j] == 2:
			start = count
		if grid[i][j] == 3 :
			end.append(count)
		if grid[i][j] != 1 :
			grid_to_state[(i,j)] = count
			state_to_grid[count] = (i,j)
			count += 1

f = open(valuefile,"r")
v_pi = [] 
for i in range(states) :
	v,pi = f.readline().split()
	v,pi = eval(v),eval(pi)
	v_pi.append([v,pi])

cur = start
path = []
while not cur in end :
	ac = v_pi[cur][1]

	(i,j) = state_to_grid[cur]
	action = []
	
	if i > 0 and grid[i-1][j] != 1 :
		action.append(0)
	if i < grid.shape[0]-1 and grid[i+1][j] != 1 :
		action.append(1)
	if j > 0 and grid[i][j-1] != 1 :
		action.append(3)
	if j < grid.shape[1]-1 and grid[i][j+1] != 1 :
		action.append(2)

	correct_prob = p + ((1-p)*1.0)/len(action)
	wrong_prob = ((1-p)*1.0)/len(action)

	prob = []
	for t in range(len(action)) :
		if action[t] == ac :
			prob.append(correct_prob)
		else :
			prob.append(wrong_prob)

	ac_prob = np.random.choice(action,1,p=prob)
	# print(action)
	# print(prob)
	# print(ac_prob)
	if ac_prob == 0 :
		path.append('N')
		cur = grid_to_state[(i-1,j)]
	elif ac_prob == 1:
		path.append('S')
		cur = grid_to_state[(i+1,j)]
	elif ac_prob == 2 :
		path.append('E')
		cur = grid_to_state[(i,j+1)]
	elif ac_prob == 3 :
		path.append('W')
		cur = grid_to_state[(i,j-1)]

print(*path)