from faker import Faker


fake = Faker()

for i in range (3):
    
    print(fake.name())
    print(fake.email())
    print(fake.country())
    print(fake.profile())
    print("\n")
