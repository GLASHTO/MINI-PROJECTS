import json 

arr = []
with open('damn.txt', encoding = 'utf-8') as f:
	for i in f:
		w = i.strip().split('\n')[0]
		if len(w) > 0:
			arr.append(w)	
	print(arr)	
with open ('damn.json','w', encoding = 'utf-8') as saved_data:
		json.dump(arr,saved_data)
		