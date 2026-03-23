from random import randint
class train :

    def __init__(self,trainno):
        self.trainno = trainno

    def book(self,fro,to):
        print(f"booking is done for {self.trainno} from {fro} to {to}")

    def timing(self):
        print(f"timing is 10:00 for {self.trainno}")

    def fare(self):
        print(f"fare is {randint(100,700)} for {self.trainno}")


train1 = train(34534545)
train1.book("delhi","mumbai")
train1.timing()
train1.fare()        

