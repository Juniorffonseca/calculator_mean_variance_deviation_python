import numpy as np


def calculate(entrada):
  if len(entrada) != 9:
    raise ValueError("List must contain nine numbers.")

  m = np.array(entrada).reshape([3, 3])
  r = {
    "mean": [m.mean(0).tolist(),
             m.mean(1).tolist(),
             m.mean()],
    "variance": [m.var(0).tolist(),
                 m.var(1).tolist(),
                 m.var()],
    "standard deviation": [m.std(0).tolist(),
                           m.std(1).tolist(),
                           m.std()],
    "max": [m.max(0).tolist(), m.max(1).tolist(),
            m.max()],
    "min": [m.min(0).tolist(), m.min(1).tolist(),
            m.min()],
    "sum": [m.sum(0).tolist(), m.sum(1).tolist(),
            m.sum()],
  }
  return r

