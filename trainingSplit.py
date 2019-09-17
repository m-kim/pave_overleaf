import numpy as np
def get_split(array_to_split, split_type):
    np.random.seed(0)
    np.random.shuffle(array_to_split)
    np.random.seed()
    split = array_to_split
    if split_type == 'train':
        split = split[:int(len(split)*0.6)]
    elif split_type == 'val':
        split = split[int(len(split)*0.6):int(len(split)*0.8)]
    elif split_type == 'test':
        split = split[int(len(split)*0.8):]
    return split
