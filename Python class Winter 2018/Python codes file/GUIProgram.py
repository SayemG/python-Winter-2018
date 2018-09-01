from breezypythongui import EasyFrame

class HelloWorld(EasyFrame):
    """Displays a greeting in a window."""

    def __init__(self):
        """Sets up the window and the label."""
        EasyFrame.__init__(self)
        
        self.addLabel(text = "First Name:", 
                      row = 0, column = 0)
        
        self.firstNameField = self.addTextField(text="",
                                              row = 0,
                                              column = 1)

        
        self.addLabel(text = "Last Name:", 
                      row = 1, column = 0)
        
        self.lastNameField = self.addTextField(text="",
                                              row = 1,
                                              column = 1)
        
        self.addLabel(text = "Title:", 
                      row = 0, column = 2)
        
        
        self.listBox = self.addListbox(row = 0, column = 3, rowspan = 2)

        self.listBox.insert(0, "Programmer")
        self.listBox.insert(0, "Manager")
        self.listBox.insert(0, "Designer")
        self.listBox.setSelectedIndex(0)
        
        self.jobTileScale = self.addScale(label = "Title",

                                         row = 2, column = 0,

                                         columnspan = 2,

                                         from_ = 50000, to = 300000,

                                         length = 300,

                                         tickinterval = 50000,

                                         command = self.showSalary)
        
        self.salaryField = self.addTextField(text="",
                                              row = 3,
                                              column = 0)
        # The command button
        self.addButton(text = "Save", row = 2, column = 2,
                       columnspan = 2, command = self.saveData)

        
    def showSalary(self, Salary):
        self.salaryField.setText("$" + Salary)
        
    def saveData(self):
        firstName = self.firstNameField.getText()
        lastName = self.lastNameField.getText()
        title = self.listBox.getSelectedItem()
        salary = self.salaryField.getText()
        #validation 
        self.messageBox(title = "Confirmation",
                            message = firstName +" "+lastName+
                       " has been added to the Database as "+
                       title+ ", with a salary of "+salary)
        
        

# Instantiates and pops up the window.
if __name__ == "__main__":
    HelloWorld().mainloop()