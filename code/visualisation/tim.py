#git branch

#nieuwe branch
#git branch tim

#ga naar branch
#git checkout tim

#git pull

#git push main
#git push origin tijmen:main

def visualise(chip, z):
    decimals = len(str(max([gate.gate_id for gate in chip.gates])))

    print_up = ""
    print_middle =""
    print_down = ""
    symbol = "░"
    left = " "
    right = " "
    forwards = " "
    backwards = " "

    for y in range(chip.height):
        print(print_up)
        print(print_middle)
        print(print_down)
        print_up = ""
        print_middle = ""
        print_down = ""

        for x in range(chip.width):
            gridpoint = chip.getGridPoint(x,y,z)

            if gridpoint.checkMoveUsed('up'):
                symbol = "U"
            if gridpoint.checkMoveUsed('down'):
                symbol = "D"
            if gridpoint.isIntersected():
                symbol = "I"
            if gridpoint.isGate():
                symbol = str(gridpoint.gate_id)
            if gridpoint.checkMoveUsed('right'):
                right = "-"
            if gridpoint.checkMoveUsed('left'):
                left = "-"
            if gridpoint.checkMoveUsed('forwards'):
                forwards = "|"
            if gridpoint.checkMoveUsed('backwards'):
                backwards = "|"

            print_up = print_up + ' ' + (decimals*forwards) + ' '
            if symbol.isnumeric():
                d = (decimals - len(symbol))
                print_middle = print_middle + left + d*"░" + symbol + right         
            else:
                print_middle = print_middle +  left + (decimals*symbol) + right
            print_down = print_down + ' ' + (decimals*backwards) + ' ' 

            symbol = "░"
            left = " "
            right = " "
            forwards = " "
            backwards = " "

    print(f"Z: {z}")