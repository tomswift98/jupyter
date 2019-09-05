import numpy
from matplotlib import pyplot

def square(x):
    return x**2

def sqrt(x):
    return numpy.sqrt(x)

def y(x):
    return 4*x+3

def plot(fn, lower=0, upper=10, by=0.05, **kwargs):
    
    options = { 
        'range' : False, 
        'title' : False, 
        'xlabel' : False, 
        'ylabel' : False, 
        'grid' : False,
        'frame' : True}

    options.update(kwargs)
    
    x = numpy.arange(lower, upper, by)
    fig = pyplot.figure()
    ax=fig.add_axes([0,0,1,1])
    
    ax.grid() if options.get('grid') != False else None
    ax.set_title(options.get('title')) if options.get('title') != False else None
    ax.set_xlabel(options.get('xlabel')) if options.get('xlabel') != False else None
    ax.set_ylabel(options.get('ylabel')) if options.get('ylabel') != False else None
    ax.set_ylim(options.get('range')) if options.get('range') != False else None
    ax.set_frame_on(False) if options.get('frame') != True else None
        
    if isinstance(fn, list):
        for f in fn:
            ax.plot(x,f(x))
    else:
        ax.plot(x,fn(x))
    
    
plot([sqrt,y],2,40,6)
