def pattern(rows, cols):
    if cols % 2 != 0:
        cu = (cols + 1) // 2
    else:
        cu = cols // 2

    if cols % 2 != 0:
        for r in range(cu):
            print(" ___", end="    ")
        print()

        for c in range(rows):
            for r in range(cu):
                if r != (cu - 1):
                    print("/   \___", end="")
                else:
                    print("/   \ ", end="")
            print()

            for r in range(cu):
                if r != (cu - 1):
                    print("\___/", end="   ")
                else:
                    print("\___/")
    else:
        for r in range(cu):
            print(" ___", end="    ")
        print()

        for c in range(rows):
            for r in range(cu):
                if r != (cu - 1):
                    print("/   \___", end="")
                elif c != 0:
                    print("/   \___/")
                else:
                    print("/   \___")
                    
            for r in range(cu):
                if r != (cu - 1):
                    print("\___/", end="   ")
                elif c != rows - 1:
                    print("\___/   \ ")
                else:
                    print("\___/    ")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
pattern(rows, cols)
