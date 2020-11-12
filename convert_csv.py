with open('example.txt', 'r') as f:
  data = f.read()[0]

data = data.split()
n_items = 76
n_examples = int(len(data)/76)

header = ','.join(['item{}'.format(i) for i n_items])

with open('data.csv', 'w') as f:
  f.write("{}\n".format(header))
  for i in range(n_examples):
    chunk = ','.join(data[i*n_items, (i+1)*n_items])
    f.write('{}\n'.format(chunk)))