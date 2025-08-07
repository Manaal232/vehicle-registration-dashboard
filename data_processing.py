import pandas as pd


df = pd.read_excel("vehicle_class_data.xlsx", engine="openpyxl", skiprows=6, header=None)

# Step 2: Set proper column names manually
df.columns = ['S_NO', 'VEHICLE_CLASS', '4WIC', 'LMV', 'MMV', 'HMV', 'TOTAL']

# Step 3: Drop rows where VEHICLE_CLASS or TOTAL is missing
df = df.dropna(subset=['VEHICLE_CLASS', 'TOTAL'])


df['TOTAL'] = df['TOTAL'].astype(str).str.replace(",", "").astype(float)


summary = df.groupby('VEHICLE_CLASS')['TOTAL'].sum().reset_index()

print("\n🚘 Summary:")
print(summary)

summary.to_excel("summary_by_vehicle_class.xlsx", index=False)
print("\n✅ Saved: summary_by_vehicle_class.xlsx")
