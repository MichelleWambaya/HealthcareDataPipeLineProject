from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_health_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "patient_id": fake.uuid4(),
            "name": fake.name(),
            "gender": random.choice(["M", "F"]),
            "date_of_birth": fake.date_of_birth(minimum_age=2, maximum_age=90),
            "address": fake.address().replace("\n", ", "),
            "phone_number": fake.phone_number(),
            "email": fake.email(),
            "insurance_provider": random.choice(["Britam", "Jubilee", "Sanlam", "CIC Insurance Group"]),
            "diagnosis": random.choice(["Diabetes", "Hypertension", "Asthma", "Healthy"]),
            "visit_date": fake.date_between(start_date='-1y', end_date='today'),
            "prescription": random.choice(["Metformin", "Lisinopril", "Albuterol", "None"])
        }
        data.append(record)
    return pd.DataFrame(data)

# Generate 10 fake patient records
df = generate_health_data(100)
print(df)
