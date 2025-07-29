# Loop Through a Dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print('key: ',x) # print key
  print('values: ',thisdict[x]) # print value


for x in thisdict.values():
  print('values: ',x)
  
for x, y in thisdict.items():
  print('items: ',x, y)
