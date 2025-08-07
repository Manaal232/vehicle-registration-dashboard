import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO


df = pd.read_excel("vehicle_growth_data.xlsx")

st.title("📊 Vehicle Registration Growth Dashboard")
st.markdown("Analyze **Year-over-Year (YoY)** and **Quarter-over-Quarter (QoQ)** growth by vehicle class.")

vehicle_classes = df["VEHICLE_CLASS"].unique().tolist()
selected_classes = st.sidebar.multiselect("Select vehicle classes:", vehicle_classes, default=vehicle_classes)

# Filter the data
filtered_df = df[df["VEHICLE_CLASS"].isin(selected_classes)]


df_sorted = filtered_df.sort_values(by=["VEHICLE_CLASS", "YEAR", "QUARTER"])
df_sorted["TOTAL"] = df_sorted["TOTAL"].astype(float)

quarter_map = {"Q1": 1, "Q2": 2, "Q3": 3, "Q4": 4}
df_sorted["Q_NUM"] = df_sorted["QUARTER"].map(quarter_map)

# Calculate QoQ Growth
df_sorted["QoQ_GROWTH_%"] = df_sorted.groupby("VEHICLE_CLASS")["TOTAL"].pct_change().fillna(0) * 100

# Calculate YoY growth (Q4 2025 vs Q4 2024)
yoy_df = df_sorted[(df_sorted["YEAR"].isin([2024, 2025])) & (df_sorted["QUARTER"] == "Q4")]
yoy_growth = (
    yoy_df.pivot(index="VEHICLE_CLASS", columns="YEAR", values="TOTAL")
    .reset_index()
    .rename(columns={2024: "Q4_2024", 2025: "Q4_2025"})
)
yoy_growth["YoY_GROWTH_%"] = ((yoy_growth["Q4_2025"] - yoy_growth["Q4_2024"]) / yoy_growth["Q4_2024"]) * 100


final_df = df_sorted.merge(yoy_growth[["VEHICLE_CLASS", "YoY_GROWTH_%"]], on="VEHICLE_CLASS", how="left")


st.subheader("📈 Growth Table")
st.dataframe(final_df[["VEHICLE_CLASS", "YEAR", "QUARTER", "TOTAL", "QoQ_GROWTH_%", "YoY_GROWTH_%"]])

# Download button
output = BytesIO()
final_df.to_excel(output, index=False, engine='openpyxl')
excel_data = output.getvalue()

st.download_button(
    label="📥 Download Growth Data (Excel)",
    data=excel_data,
    file_name="vehicle_growth_output.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)


st.subheader("📊 Growth Trend Chart (2025)")
chart_data = final_df[final_df["YEAR"] == 2025]

fig, ax = plt.subplots()
for name, group in chart_data.groupby("VEHICLE_CLASS"):
    ax.plot(group["QUARTER"], group["TOTAL"], marker='o', label=name)

ax.set_xlabel("Quarter")
ax.set_ylabel("Registrations")
ax.set_title("Quarterly Vehicle Registrations - 2025")
ax.legend()
st.pyplot(fig)
