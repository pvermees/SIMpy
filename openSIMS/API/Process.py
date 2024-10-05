import copy
import openSIMS as S
from . import Geochron, Stable

class Samples:

    def __init__(self,simplex,method):
        self.pars = simplex.get_pars(method)
        self.method = method
        self.samples = copy.copy(simplex.samples)

class GeochronSamples(Samples,Geochron.Geochron,Geochron.Processor):
    pass

class StableSamples(Samples,Stable.Stable,Stable.Processor):
    pass

def get_samples(simplex,method=None):
    if method is None:
        method = list(simplex.methods.keys())[0]
    datatype = S.settings(method)['type']
    if datatype == 'geochron':
        return GeochronSamples(simplex,method)
    elif datatype == 'stable':
        return StableSamples(simplex,method)
    else:
        raise ValueError('Unrecognised data type')
