import pandas as pd
import random

# Load your cleaned 2025 summary data
df = pd.read_excel("summary_by_vehicle_class.xlsx")

# Simulate quarterly data
growth_data = []
for _, row in df.iterrows():
    vehicle_class = row['VEHICLE_CLASS']
    total_2025 = row['TOTAL']

    # Randomly break 2025 total into 4 quarters
    q1 = random.randint(int(total_2025 * 0.15), int(total_2025 * 0.30))
    q2 = random.randint(int(total_2025 * 0.15), int(total_2025 * 0.30))
    q3 = random.randint(int(total_2025 * 0.15), int(total_2025 * 0.30))
    q4 = total_2025 - q1 - q2 - q3

    # Mock 2024 Q4 as slightly lower than 2025 Q4
    q4_2024 = int(q4 * random.uniform(0.7, 0.95))

    # Append 5 entries per vehicle class
    growth_data.extend([
        {'VEHICLE_CLASS': vehicle_class, 'YEAR': 2024, 'QUARTER': 'Q4', 'TOTAL': q4_2024},
        {'VEHICLE_CLASS': vehicle_class, 'YEAR': 2025, 'QUARTER': 'Q1', 'TOTAL': q1},
        {'VEHICLE_CLASS': vehicle_class, 'YEAR': 2025, 'QUARTER': 'Q2', 'TOTAL': q2},
        {'VEHICLE_CLASS': vehicle_class, 'YEAR': 2025, 'QUARTER': 'Q3', 'TOTAL': q3},
        {'VEHICLE_CLASS': vehicle_class, 'YEAR': 2025, 'QUARTER': 'Q4', 'TOTAL': q4},
    ])

# Create DataFrame and save
growth_df = pd.DataFrame(growth_data)
growth_df.to_excel("vehicle_growth_data.xlsx", index=False)

print("✅ vehicle_growth_data.xlsx created with simulated quarterly data.")
