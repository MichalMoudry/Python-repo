class UserInterface():
    @staticmethod
    def PrintHeader(Index, HeaderToBePrinted, IsFirst):
        HEADER = ""
        if IsFirst == False:
            HEADER = HEADER + "\n"

        HEADER = HEADER + "----- "
        
        if Index != "":
            HEADER = HEADER + Index + "."

        HEADER = HEADER + HeaderToBePrinted
        HEADER = HEADER + " -----"
        print(HEADER)