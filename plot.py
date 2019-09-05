import numpy
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 2D plot function
# input a function name or array of function names and a single domain array [lower, upper]
# additional options can be set using keyword arguments
def plot(fn, domain, **kwargs):
    options = { 
        'range' : False, 
        'title' : False, 
        'xlabel' : False, 
        'ylabel' : False, 
        'grid' : False,
        'frame' : True,
        'points' : 1000}

    options.update(kwargs)

    resolution = options.get('points')
    x = numpy.linspace(domain[0], domain[1], resolution)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    
    ax.grid() if options.get('grid') != False else None
    ax.set_title(options.get('title')) if options.get('title') != False else None
    ax.set_xlabel(options.get('xlabel')) if options.get('xlabel') != False else None
    ax.set_ylabel(options.get('ylabel')) if options.get('ylabel') != False else None
    ax.set_ylim(options.get('range')) if options.get('range') != False else None
    ax.axis('off') if options.get('frame') != True else ax.axis('on')
        
    if isinstance(fn, list):
        for f in fn:
            ax.plot(x,f(x))
    else:
        ax.plot(x,fn(x))

# 3D plot function
# input a function name or array of function names and two domain arrays [lower, upper] 
# additional options can be set using keyword arguments
def plot3D(fn, xdomain, ydomain, **kwargs):
    options = { 
        'title' : False, 
        'xlabel' : False, 
        'ylabel' : False,
        'zlabel' : False, 
        'frame' : True,
        'points' : 500,
        'contours' : 50,
        'view' : [40,35]}
    
    options.update(kwargs)
    
    resolution = options.get('points')
    
    x = numpy.linspace(xdomain[0], xdomain[1], resolution)
    y = numpy.linspace(ydomain[0], ydomain[1], resolution)

    X,Y = numpy.meshgrid(x,y)
    Z = fn(X,Y)
    
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.contour3D(X, Y, Z, options.get('contours'))
    
    ax.view_init(options.get('view')[0],options.get('view')[1])
    ax.set_title(options.get('title')) if options.get('title') != False else None
    ax.set_xlabel(options.get('xlabel')) if options.get('xlabel') != False else None
    ax.set_ylabel(options.get('ylabel')) if options.get('ylabel') != False else None
    ax.set_zlabel(options.get('zlabel')) if options.get('zlabel') != False else None
    ax.set_ylim(options.get('range')) if options.get('range') != False else None
