from appJar import gui

from sympy import *

from sympy.calculus.util import continuous_domain

from sympy.plotting import plot

import pyautogui





def getFocus():

    app.setEntryFocus("function")

    pyautogui.press("left")

    pass





def asin():

    text = str(app.getEntry("function"))

    app.setEntry("function", "".join((text, "asin()")))

    getFocus()

    pass



def acos():

    text = str(app.getEntry("function"))

    app.setEntry("function", "".join((text, "acos()")))

    getFocus()







def atan():

    text = str(app.getEntry("function"))

    app.setEntry("function", "".join((text, "atan()")))

    getFocus()







def acot():

    text = str(app.getEntry("function"))

    app.setEntry("function", "".join((text, "acot()")))

    getFocus()





def abs():

    text = str(app.getEntry("function"))

    app.setEntry("function", "".join((text, "Abs()")))

    getFocus()







def sin():

    text = str(app.getEntry("function"))

    app.setEntry("function", "".join((text, "sin()")))

    getFocus()





def cos():

    text = str(app.getEntry("function"))

    app.setEntry("function", "".join((text, "cos()")))

    getFocus()





def tan():

    text = str(app.getEntry("function"))

    app.setEntry("function", "".join((text, "tan()")))

    getFocus()





def cot():

    text = str(app.getEntry("function"))

    app.setEntry("function", "".join((text, "cot()")))

    getFocus()





def log():

    text = str(app.getEntry("function"))

    app.setEntry("function", "".join((text, "log()")))

    getFocus()





def ln():

    text = str(app.getEntry("function"))

    app.setEntry("function", "".join((text, "ln()")))

    getFocus()





def pow():

    text = str(app.getEntry("function"))

    app.setEntry("function", "".join((text, "**")))

    app.setEntryFocus("function")





def root():

    text = str(app.getEntry("function"))

    app.setEntry("function", "".join((text, "sqrt()")))

    getFocus()



def makePlot(sympy_exp):

    x = symbols('x')

    if "Abs" in str(sympy_exp):

        p1 = plot(sympy_exp,  (x, -1000,1000), 0.01, size= (7,7), xlim=(-10, 10), ylim=(-10, 10), legend=True, ylabel='y', line_color='green', label='f(x)', show=False)

    else:

        p1 = plot(sympy_exp, (x, -1000, 1000), 0.01, size=(7, 7), xlim=(-10, 10), ylim=(-10, 10), legend=True,

                  ylabel='y', line_color='green', label='f(x)', show=False)

        p1.extend(plot(diff(sympy_exp, x), (x, -1000,1000), 0.01, xlim=(-10, 10), ylim=(-10, 10), legend=True, ylabel='y', label="f'(x)", line_color='red', show=False))

    p1.show()



def properties(sympy_exp):

    x = symbols('x')

    if "Abs" in str(sympy_exp):

        x = symbols('x', real=True)

        func = "f(x) = " + str(sympy_exp)

        dziedzina = "x e = " + str(continuous_domain(sympy_exp, x, S.Reals))

        txt = func + dziedzina

        app.setMessage("s1", txt)

    else:

        dx = "f'(x) = " + str(diff(sympy_exp, x))

        func = "f(x) = " + str(sympy_exp)

        dziedzina = "x e = " + str(continuous_domain(sympy_exp, x, S.Reals))

        mz = "mz = " + str(solve(sympy_exp, x))

        txt = func + dziedzina

        app.setMessage("s1", txt)

        print(dx)

    print(func)

    print(mz)

    print(dziedzina)

    #app.changeSpinBox("s1", [func, mz, dziedzina, dx], reverse = True)



def setPlot():

    equation = app.getEntry("function")

    try:

        sympy_exp = parse_expr(equation)

    except:

        app.errorBox("Error", "Incorrectly typed equation  :(")

        app.setFocus("function")

    makePlot(sympy_exp)

    properties(sympy_exp)

    print(sympy_exp)

    getFocus()

    pass



def clear():

    app.setEntry("function", "")

    getFocus()

    pass



def setApp():

    app.setResizable(False)

    app.setTitle("Powerful beta 2.0")

    app.setSize(500, 700)

    app.setLocation(100, 100)

    app.setSticky("news")

    app.setExpand("both")

    app.setFont(15)

    pass



def setAllEntries():

    app.addEntry("function", 0, 0, 4)

    app.addButton("sin", sin, 1, 0)

    app.addButton("cos", cos, 1, 1)

    app.addButton("tan", tan, 1, 2)

    app.addButton("cot", cot, 1, 3)

    app.addButton("asin", asin, 2, 0)

    app.addButton("acos", acos, 2, 1)

    app.addButton("atan", atan, 2, 2)

    app.addButton("acot", acot, 2, 3)

    app.addButton("log", log, 3, 0)

    app.addButton("Abs", abs, 3, 1)

    app.addNamedButton("aˣ", "pow", pow, 3, 2)

    app.addNamedButton("√", "root", root, 3, 3)

    app.addButton("Draw", setPlot, 4, 0, 3)

    app.addButton("C", clear, 4, 3)

    #app.addMessage("s1", "f(x)=\nroots=\nx ∈ =\nf'(x)=\n", 5, 0, 4)

    pass



app = gui()

setApp()

setAllEntries()

app.go()
