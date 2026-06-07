import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

n = 50000

countries = ['Germany','Turkey','UAE','Saudi Arabia','Taiwan','Bangladesh','Bosnia']
cuisines = ['Italian','Turkish','Asian','Fast Food','Healthy','Mexican','Indian','Dessert']
cities = ['Berlin','Istanbul','Dubai','Riyadh','Taipei','Dhaka','Sarajevo']
vendor_tiers = ['Premium','Standard','Budget']

vendors = pd.DataFrame({
    'vendor_id': [f'V{str(i).zfill(5)}' for i in range(1, 1001)],
    'vendor_name': [f'Restaurant_{i}' for i in range(1, 1001)],
    'country': np.random.choice(countries, 1000),
    'city': np.random.choice(cities, 1000),
    'cuisine_type': np.random.choice(cuisines, 1000),
    'vendor_tier': np.random.choice(vendor_tiers, 1000, p=[0.2, 0.5, 0.3]),
    'joined_date': [
        (datetime(2020,1,1) + timedelta(days=random.randint(0,1460))).strftime('%Y-%m-%d')
        for _ in range(1000)
    ],
    'avg_prep_time_min': np.random.randint(10, 45, 1000),
    'rating': np.round(np.random.uniform(2.5, 5.0, 1000), 1),
    'is_active': np.random.choice([1, 0], 1000, p=[0.85, 0.15])
})

start_date = datetime(2023, 1, 1)
orders = pd.DataFrame({
    'order_id': [f'ORD{str(i).zfill(7)}' for i in range(1, n+1)],
    'vendor_id': np.random.choice(vendors['vendor_id'], n),
    'order_date': [
        (start_date + timedelta(days=random.randint(0,730))).strftime('%Y-%m-%d')
        for _ in range(n)
    ],
    'item_count': np.random.randint(1, 8, n),
    'gross_order_value': np.round(np.random.uniform(5, 120, n), 2),
    'delivery_fee': np.round(np.random.uniform(0, 5.99, n), 2),
    'discount_amount': np.round(np.random.uniform(0, 15, n), 2),
    'is_cancelled': np.random.choice([0, 1], n, p=[0.92, 0.08]),
    'payment_method': np.random.choice(['card','cash','wallet'], n, p=[0.6,0.2,0.2]),
    'customer_id': [f'C{str(random.randint(1,15000)).zfill(6)}' for _ in range(n)]
})

orders['net_order_value'] = np.round(
    orders['gross_order_value'] - orders['discount_amount'], 2
)
orders['affordability_score'] = np.round(
    1 - (orders['gross_order_value'] / orders['gross_order_value'].max()), 3
)

vendors.to_csv('data/raw/vendors.csv', index=False)
orders.to_csv('data/raw/orders.csv', index=False)
print(f"✅ vendors.csv: {len(vendors)} rows")
print(f"✅ orders.csv: {len(orders)} rows")
