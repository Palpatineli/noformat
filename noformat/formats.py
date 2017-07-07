from collections import namedtuple

import numpy as np

FileFormat = namedtuple('FileFormat', ['ext', 'is_', 'save', 'load'])

np_array_ext = '.npy'
np_array = FileFormat(np_array_ext,
                      lambda x: isinstance(x, np.ndarray),
                      lambda name, value: np.save(name + np_array_ext, value),
                      lambda name: np.load(name + np_array_ext))

np_arrays_ext = '.npz'
np_arrays = FileFormat(np_arrays_ext,
                       lambda x: isinstance(x, dict) and all([isinstance(value, np.ndarray) for value in x.values()]),
                       lambda name, value: np.savez_compressed(name + np_arrays_ext, **value),
                       lambda name: np.load(name + np_arrays_ext))

try:
    import pandas as pd

    pd_ext = '.msg'
    pd_data = FileFormat(pd_ext,
                         lambda x: isinstance(x, pd.DataFrame),
                         lambda name, value: pd.to_msgpack(name + pd_ext, value),
                         lambda name: pd.read_msgpack(name + pd_ext))
except ImportError:
    pd = None
    pd_data = None

formats = {cls.ext: cls for cls in [np_array, np_arrays, pd_data] if cls is not None}
