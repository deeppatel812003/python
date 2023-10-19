class Railwayform:
    formtype = "Railwayform"
    def printdata(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
application = Railwayform()
application.name = "deep"
application.train = "haridwar"
application.printdata()