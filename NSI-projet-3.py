'''
'''


with open("Characters.csv", mode = "r", encoding = "utf-8") as f:
    text = csv.DictReader(f, delimiter=';')
    csv1 = [{key : value for key, value in element.items()} for element in text]

with open(".csv", mode = "r", encoding = "utf-8") as f:
