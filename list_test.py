bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[1].title()}."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

cars = ['bmw', 'toyota', 'audi', 'subaru']
cars.sort(reverse=False)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse=True))
print("\nHere is the original list again:")
print(cars)
print(len(cars))

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)