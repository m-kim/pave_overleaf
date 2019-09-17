import PAVE
from torch.utils.data import DataLoader

def load_data(visualisation_vars=None, path = None):
    if path:
        train_set  = PAVE.DataLoader(path)
        train_data = DataLoader(dataset = train_set)
        return train_data
    else:
        PAVE.open(visualisation_vars)
        
def train(Model, simulation_variables):
    for (i, var) in enumerate(visualisation_vars):
        train_sample = load_data(var)
        prediction = Model(train_sample)
        ...
