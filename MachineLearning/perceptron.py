from bokeh.plotting import figure, output_file, show

'''
# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("lines.html", title="line plot example")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend="Temp.", line_width=2)

# show the results
show(p)
'''


def dot(v1, v2):
    return sum([v1[i]*v2[i] for i in range(len(v1))])


def sign(el):
    if el < 0:
        return -1
    else:
        return 1


def perceptron(x_y_list, w, lr):
    for x, y in x_y_list:
        perceptronR((x, y), w, lr)


def perceptronR(x_y, w, lr):
    ynext = dot(x_y[0], w)
    print(sign(ynext))
    if sign(ynext) != x_y[1] or ynext == 0:
        for i in range(len(w)):
            w[i] = w[i] + lr*x_y[1]*x_y[0][i]
        perceptronR(x_y, w, lr)

if __name__ == '__main__':
    listOfPositivePoint = [([5, 4], +1), ([6, 7], +1), ([7, 7], +1)]
    listOfNegativePoint = [([1, 2], -1), ([3, 4], -1), ([2, 0], -1)]
    x_y = listOfNegativePoint + listOfPositivePoint
    print(x_y)
    w = [0, 0]
    lr = 0.1
    perceptron(x_y, w, lr)
    print(w)
    x1 = [x[0] for x, y in listOfPositivePoint]
    y1 = [x[1] for x, y in listOfPositivePoint]
    x2 = [x[0] for x, y in listOfNegativePoint]
    y2 = [x[1] for x, y in listOfNegativePoint]
    x3 = -10
    x4 = 10
    y3 = -(w[0]/w[1])*(x3)
    y4 = -(w[0]/w[1])*(x4)
    x = [x3, x4]
    y = [y3, y4]
    output_file("line.html")
    p = figure(plot_width=400, plot_height=400)

    # add a circle renderer with a size, color, and alpha
    p.circle(x1, y1, size=5, color="navy", alpha=0.5)
    p.circle(x2, y2, size=5, color="red", alpha=0.5)
    p.line(x, y, legend="Temp.", line_width=2)

    # show the results
    show(p)
