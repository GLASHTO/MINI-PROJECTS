import json 

arr = []
with open('damn.txt', encoding = 'utf-8') as f:
	for i in f:
		w = i.split('\n')[0]
		if w != '' or w != '\n' or w !=' ':
			arr.append(w)	
	print(arr)	
with open ('damn.json','w', encoding = 'utf-8') as saved_data:
		json.dump(arr,saved_data)
		