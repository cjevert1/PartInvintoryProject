"""Clayton Evert
this program will be for parts invintory it will let you add a part to the list
let you remove the part from the invinntory search for a part 
or let you see the whole list of parts in stock"""

from breezypythongui import EasyFrame

class PartsInvintory(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Parts Invintory System")
        self.addLabel(text="What would you like to do: ", row=0, column=0,
                      sticky="NSEW", columnspan=2,)
        self.addButton(text="Add Part",row=1,column=0, command=self.AddPart)
        self.addButton(text="Remove Part",row=1,column=1,command=self.RemPart)
        self.addButton(text="Search for part",row=2,column=0,command=self.SerchPart)
        self.addButton(text="Show all",row=2,column=1,command=self.allPart)

    #this will be for adding a part
    def AddPart(self):
        part = self.prompterBox(title="Add Part",
                                promptString="Part Number: ")
        
    #this will be for removing a part
    def RemPart(self):
        part = self.prompterBox(title="Remove Part",
                                promptString="Part Number: ")
    #this will be for searching for a part
    def SerchPart(self):
        part = self.prompterBox(title="Search Part",
                                promptString="Part Number: ")

    #this will show all available parts
    def allPart(self):
        print("This will open a window to show all available parts")


def main():
    PartsInvintory().mainloop() 

if __name__ == "__main__":
    main()