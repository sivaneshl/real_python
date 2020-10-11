import faker
import random
import datetime

faker = faker.Faker()

def first_name_and_gender():
    # Link first name and gender 
    gender = 'M' if random.randint(0, 1) == 0 else 'F'
    fname = faker.first_name_male() if gender == 'M' else faker.first_name_female()
    return {'gender': gender, 'name': fname}

def birth_date_and_start_date():
    # Link birth date and start date 
    start_date = faker.date_between(start_date='-20y', end_date='now')    
    delta = datetime.timedelta(days=365 * random.randint(18, 40))  # 18y-40y
    birth_date = start_date - delta
    return {'birth_date': birth_date, 'start_date': start_date}

def salary_and_bonus():
    salary = round(random.randint(90000, 120000) / 1000) * 1000
    bonus_ratio = random.uniform(0.15, 0.2)
    bonus = (salary * bonus_ratio / 500) * 500 
    return {'salary': salary, 'bonus': bonus}

data = dict()
data['first_name_and_gender'] = first_name_and_gender
data['last_name'] = lambda: {'last_name': faker.last_name()}
data['email_address'] = lambda: {'email_address': faker.email()}
data['ssn'] = lambda: {'ssn': faker.ssn()}
data['birth_data_and_start_date'] = birth_date_and_start_date
data['address'] = lambda: {'address': faker.address()}
data['office'] = lambda: {'office': faker.city()}
data['title'] = lambda: {'title': faker.job()}
data['salary_and_bonus'] = salary_and_bonus

# print([data[k]() for k in data.keys()])

for i in range(10):
    result = [list(data[k]().values()) for k in data.keys()]
    row = [item for sublist in result for item in sublist]
    print(row)
    
