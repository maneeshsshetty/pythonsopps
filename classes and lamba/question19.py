colors = ['red', 'black', 'white', 'green', 'orange']
substring = "ack"
result = list(filter(lambda x: substring in x, colors))
print("Words with 'ack':", result)
