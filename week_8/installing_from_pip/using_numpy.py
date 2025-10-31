try:
    import numpy as np
    arr = np.array([1, 2, 3])
    print('Array:', arr)
    print('Mean:', np.mean(arr))
except Exception as e:
     print('Numpy not available. Install with pip and retry.\n', e)
