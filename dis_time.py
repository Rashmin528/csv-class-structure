def calculate_time(graph, path):
	Total_time = 0.0
	for x in range(0,len(path)-1):
		segment_list = graph[path[x]]
		for neighbor in segment_list:
			if neighbor.end_city == path[x+1]:
				Total_time = Total_time + int(neighbor.distance)/int(neighbor.maxspeed)
	return Total_time
