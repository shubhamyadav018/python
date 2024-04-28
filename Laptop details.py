class Card:
    def _init_(self , imageurl , price,rating,description,deliverywithin,comments,brandname):
        self.imageurl=imageurl
        self.price=price
        self.rating=rating
        self.description=description
        self.deliverywithin=deliverywithin
        self.comments=comments
        self.brandname=brandname

    def printAllDetails(self):
        print("product brand is :", self.brandname)
        print("product brand is :", self.price)
        print("product brand is :", self.rating)


commentforlaptop = ["This is good","okay","not good"]
laptop = Card("dummy-url-1",90000,4.5,"This is not good performance")
laptop.printAllDetails()

commentformobile = ["battery is draining ", ]
