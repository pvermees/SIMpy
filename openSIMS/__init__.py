import matplotlib.pyplot as plt
from .API import Simplex, Settings
from .GUI.Main import gui

__simplex = Simplex.Simplex()
__settings = Settings.Settings()

def set(prop,val):
    setattr(__simplex,prop,val)

def get(prop):
    return getattr(__simplex,prop)

def method(method,**kwargs):
    __simplex.method = method
    __simplex.channels = __settings.ions2channels(method,**kwargs)

def standards(**kwargs):
    __simplex.set_groups(**kwargs)
    
def reset():
    __simplex.reset()

def read():
    __simplex.read()

def calibrate():
    __simplex.calibrate()

def view(i=None,sname=None,show=True):
    if i is None and sname is None:
        i = __simplex.i
    fig, ax = __simplex.view(i=i,sname=sname)
    if show: plt.show()
    return fig, ax

def plot(show=True):
    fig, ax = __simplex.plot()
    if show: plt.show()
    return fig, ax

def simplex():
    return __simplex

def settings(method):
    return __settings[method]

def TODO():
    pass
