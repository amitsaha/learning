'''
Henon function - strange attractor animation
Thanks to https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/ for matplotlib + animation stuff
'''

import matplotlib.pyplot as plt
from matplotlib import animation

def transform1(p):
    x,y  = p
    x1 = y + 1.0 - 1.4*x**2
    y1 = 0.3*x

    return x1, y1

def update_points(i, x, y, plot):
    plot.set_data(x[:i], y[:i])
    return plot,
    
if __name__ == '__main__':
    p = (0, 0)
    x = [p[0]]
    y = [p[1]]
    for i in range(10000):
        p = transform1(p)
        x.append(p[0])
        y.append(p[1])

    fig = plt.gcf()
    ax = plt.axes(xlim = (min(x), max(x)),
                  ylim = (min(y), max(y)))
    plot, = ax.plot([], [], 'o')
    anim = animation.FuncAnimation(fig, update_points,
                                   fargs=(x, y, plot),
                                   frames = len(x),
                                   interval = 25,
                                   blit = True)
    plt.title('Henon function')
    anim.save('henon_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
    plt.show()
