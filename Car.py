class Car( object ):
    def __init__( self, brand = "", price = 1, speed = 100, fuel = 10, mileage = 20000, tax = 0.12 ):
        self.brand = brand
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax
        if price > 10000:
            self.tax = 0.15
        self.display_all()
    def display_all( self ):
        # print dir( self )
        print " "
        print "Brand:", self.brand
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax
        return ( self )

Car1 = Car( "Honda", 15000, 160, "Half tank", 12000)
Car2 = Car( "Ford", 8000, 140, "Full tank", 150000)
Car3 = Car( "Hynday", 3000, 160, "Quarter tank", 25000)
Car4 = Car( "Honda", 15000, 160, "Half tank", 12000)
Car5 = Car( "Honda", 15000, 160, "Half tank", 12000)
Car6 = Car( "Honda", 15000, 160, "Half tank", 12000)

# Car1.display_all()
# Car2.display_all()
# Car3.display_all()
# Car4.display_all()
# Car5.display_all()
# Car6.display_all()