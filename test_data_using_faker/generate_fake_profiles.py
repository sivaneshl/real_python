import pandas as pd
from faker import Faker

fake = Faker()

# generate fake profiles
# print(fake.profile())

data = [fake.profile() for i in range(10)]
df = pd.DataFrame(data)
print(df)




