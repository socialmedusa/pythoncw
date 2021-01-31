from graphics import *

def cw():
    colourSelection = []
    colourSelect(colourSelection)
    size = patchSize()
    win = GraphWin("Patchwork Coursework", size * 100, size * 100)
    pattern = matrix(size)

    for p in range(size):
        line = pattern[p]
        for i in range(size):
            if line[i] == 1 or line[i] == 2:
                crossLines(0 + i*100, 0 + p * 100, colourSelection[line[i]], win)
            elif line[i] == 0:
                triangle(0 + i * 100, 0 + p * 100, colourSelection[line[i]], win)

    win.getMouse()
    win.close()


def matrix(size):

    # Pattern for 5x5 patchwork
    fivePattern = [1,0,0,0,1,
                   2,1,0,1,2,
                   2,2,1,2,2,
                   2,1,0,1,2,
                   1,0,0,0,1]

    fiveMatrix = [fivePattern[i:i+size] for i in range(0,len(fivePattern),size)]
    # Pattern for 7x7 patchwork
    sevenPattern = [1,0,0,0,0,0,1,
                    2,1,0,0,0,1,2,
                    2,2,1,0,1,2,2,
                    2,2,2,1,2,2,2,
                    2,2,1,0,1,2,2,
                    2,1,0,0,0,1,2,
                    1,0,0,0,0,0,1]

    sevenMatrix = [sevenPattern[i:i+size] for i in range(0,len(sevenPattern),size)]
    # Pattern for 9x9 patchwork
    ninePattern = [1,0,0,0,0,0,0,0,1,
                   2,1,0,0,0,0,0,1,2,
                   2,2,1,0,0,0,1,2,2,
                   2,2,2,1,0,1,2,2,2,
                   2,2,2,2,1,2,2,2,2,
                   2,2,2,1,0,1,2,2,2,
                   2,2,1,0,0,0,1,2,2,
                   2,1,0,0,0,0,0,1,2,
                   1,0,0,0,0,0,0,0,1,]

    nineMatrix = [ninePattern[i:i+size] for i in range(0,len(ninePattern),size)]
    # Return the correct pattern based on the "size variable assignment"
    if size == 5:
        return fiveMatrix
    elif size == 7:
        return sevenMatrix
    elif size == 9:
        return nineMatrix
    else:
        #Error handling
        print("An error has occured, please try again: ")
        #Restart program
        return cw()

# Line Patch taking 4 arguments (Patch X position, Patch Y position, Colour,
# Window to draw to)
def crossLines(x1, y1, colour, win):
    for x in range(5, 100, 10):
        for y in range(5, 100,10):
            line = Line(Point(x + x1 , 0 + y1), Point(100 - x + x1, 100 + y1))
            line1 = Line(Point(0 + x1, 100 - y + y1), Point(100 + x1, y + y1))
            line.draw(win)
            line.setFill(colour)
            line1.draw(win)
            line1.setFill(colour)

# Triangle patch taking 4 arguments (Patch X position, Patch Y position, Colour,
# Window to draw to)
def triangle(x1, y1, colour, win):
    x = 0
    y = 0
    for z in range(3):
        for p in range(5):
            # Draw the first triangle type (3 Points)
            tri = Polygon(Point(10 + x + x1, 0 + y + y1),
                          Point(0 + x + x1, 20 + y + y1),
                          Point(20 + x + x1, 20 + y + y1))
            tri.draw(win)
            tri.setFill(colour)
            # Set triangle outline to the colour argument
            tri.setOutline(colour)

            if z < 2:
                tri = Polygon(Point(10 + x + x1, 40 + y + y1),
                              Point(0 + x + x1, 20 + y + y1),
                              Point(0 + x + x1, 40 + y + y1),
                              Point(20 + x + x1, 40 + y + y1),
                              Point(20 + x + x1, 20 + y + y1))
                tri.draw(win)
                tri.setFill(colour)
                tri.setOutline(colour)
            x = x + 20

        x = 0
        y = y + 40


def colourSelect(colourSelection):
    validColours = ["red", "blue", "orange", "green", "cyan", "magenta"]
    colour = input("Select a colour: ")
    colour = colour.lower()

    if colour in colourSelection:
        print("Colour has already been selected, please choose a different one.")
        return colourSelect(colourSelection)

    elif colour in validColours:
        colourSelection.append(colour)

        if len(colourSelection) < 3:
            print("===============")
            print("Select colour", len(colourSelection) + 1)
            print("===============")

            return colourSelect(colourSelection)

        elif len(colourSelection) == 3:
            return colourSelection

    else:
        print("Error, That was not a valid colour.")
        colourSelect(colourSelection)


def patchSize():
    patchList = ['5', '7', '9']
    size = input("Enter a patch size [5, 7, 9]:")

    if size in patchList:
        return int(size)
    else:
        print("Error, the value is not valid")
        return patchSize()


cw()
