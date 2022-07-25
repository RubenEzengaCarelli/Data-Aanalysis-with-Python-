import numpy as np

def calculate(list):
  array = np.array(list)
  array1 = array.reshape((3, 3))

  v1 = array1[0, :]
  v2 = array1[1, :]
  v3 = array1[2, :]
  v4 = array1[:, 0]
  v5 = array1[:, 1]
  v6 = array1[:, 2]

  dict = {
  'mean': [[np.mean(v1), np.mean(v2), np.mean(v3)], [np.mean(v4), np.mean(v5), np.mean(v6)], np.mean(array1)],
  'variance': [[np.var(v1), np.var(v2), np.var(v3)], [np.var(v4), np.var(v5), np.var(v6)], np.var(array1)],
  'standard deviation': [[np.std(v1), np.std(v2), np.std(v3)], [np.std(v4), np.std(v5), np.std(v6)], np.std(array1)],
  'max': [[np.max(v1), np.max(v2), np.max(v3)], [np.max(v4), np.max(v5), np.max(v6)], np.max(array1)],
  'min': [[np.min(v1), np.min(v2), np.min(v3)], [np.min(v4), np.min(v5), np.min(v6)], np.min(array1)],
  'sum': [[np.sum(v1), np.sum(v2), np.sum(v3)], [np.sum(v4), np.sum(v5), np.sum(v6)], np.sum(array1)]
}
  
  print(dict)