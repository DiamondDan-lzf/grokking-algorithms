states_needed = set(["mt","wa","or","id","nv","ut","cat","az"])

stations = {}
stations["kone"] = set(["id","nv","ut"])
stations["ktwo"] = set(["wa","id","mt"])
stations["kthree"] = set(["or","ca","nv"])
stations["kfour"] = set(["nv","ut"])
stations["kfive"] = set(["ca","az"])

#设置一个集合来存储最终选择的广播台，集合为不会有重复的一个数组？用set()

final_stations = set()

while states_needed:
	best_station = None
	states_covered = set()
	for station, states in stations.items():
		covered = states_needed & states
		if len(covered) > len(states_covered):
			best_station = station
			states_covered = covered

	states_needed -= states_covered
	final_stations.add(best_station)

print(final_stations)

	
		



                    
