import sys
import numpy as np

### Read MDP

mdpfile = sys.argv[1]
f = open(mdpfile,"r")

strst,states = f.readline().split()
states = eval(states)

strac,actions = f.readline().split()
actions = eval(actions)

strstart,start = f.readline().split()
start = eval(start)

strend = f.readline().split()
end = [eval(el) for el in strend[1:]]

transition = {}
for i in range(states) :
	transition[i] = {}

strsplit = f.readline().split()
while strsplit[0] == "transition" :
	s1 = eval(strsplit[1])
	ac = eval(strsplit[2])
	s2 = eval(strsplit[3])
	r = eval(strsplit[4])
	p = eval(strsplit[5])

	if ac in transition[s1] :
		transition[s1][ac].append((s2,r,p))
	else :
		transition[s1][ac] = [(s2,r,p)]

	strsplit = f.readline().split()

disc = eval(strsplit[1])

# print(states,start,end,transition,disc)

#### Value Iteration ################

V = np.zeros(states)
Ac = -np.ones(states)

t = 0
while True :
	changed = False
	Ac_t = -np.ones(states)
	for i in range(states) :
		if i in end :
			continue
		trans_i = transition[i]
		maxR = -np.inf
		maxAction = -1
		for j in range(len(trans_i)) :
			action = list(trans_i)[j]
			distr = trans_i[action]
			unzip = list(zip(*distr))
			s2 = np.array(unzip[0])
			r = np.array(unzip[1])
			p = np.array(unzip[2])
			Vprev = V[s2]
			Vnext = np.sum(p*(r + disc*Vprev))
			if Vnext >= maxR :
				maxR = Vnext
				maxAction = action
		if abs(maxR - V[i]) >= pow(10,-16) :
			V[i] = maxR 
			Ac[i] = maxAction
			changed = True
	# print(V)
	t += 1
	if not changed :
		break
for i in range(states) :
	print(V[i],int(Ac[i]))
print("iterations",t)