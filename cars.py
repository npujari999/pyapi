my_cars = ["bmw", "audi", "porsche"]

dream_cars = ["lambo", "bugatti", "bentley"]

more_likely = ["ford", "toyota", "honda"]

my_cars.append(dream_cars)

my_cars.extend(more_likely)

print(my_cars)

for car in my_cars:
    if isinstance(car, list):
        for inner in car:
            if inner == "bentley":
                print(inner)
            elif inner == "toyota":
                print(inner)    
    else:
        if car == "bentley":
            print(car)
        elif car == "toyota":
            print(car)

print("Slice way")
print(my_cars[3][2])
print(my_cars[5])

