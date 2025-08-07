# 🚗 Vehicle Registration Growth Dashboard

An interactive web dashboard to analyze **Year-over-Year (YoY)** and **Quarter-over-Quarter (QoQ)** growth in vehicle registrations using VAHAN data.

> ✅ Built with Python, Pandas, and Streamlit  
> 📊 Uploads real-world data and computes insights for each vehicle class  
> 📥 Downloadable Excel reports

---

## 📌 Features

- 📂 Uploads and cleans vehicle class data (Excel format)
- 📈 Calculates:
  - **QoQ Growth %** – Quarter-over-Quarter changes in registration counts
  - **YoY Growth %** – Year-over-Year changes (Q4 to Q4)
- 🎯 Filter by **Vehicle Class**
- 📉 Interactive charts showing quarterly growth
- 📁 Download processed data as Excel file

---

## 🛠️ Tech Stack

| Component       | Tool/Library        |
|----------------|---------------------|
| Language        | Python 3            |
| Data Handling   | Pandas              |
| Visualization   | Matplotlib          |
| Web UI          | Streamlit           |
| File Export     | OpenPyXL            |

---

## 📂 Folder Structure
vehicle_dashboard/
│
├── app.py # Streamlit frontend
├── data_processing.py # Excel loading, cleaning, and saving
├── vehicle_class_data.xlsx # Raw input Excel data
├── summary_by_vehicle_class.xlsx # Cleaned data output
├── growth_data.xlsx # Final processed data
├── README.md
└── requirements.txt



---How to Run the Project

1. Clone the repository
```bash
git clone https://github.com/your-username/vehicle-dashboard.git
cd vehicle-dashboard
2. Install dependencies
pip install -r requirements.txt
3. Run the dashboard
streamlit run app.py

 Sample Insights
🚘 Private Service Vehicles saw 62% QoQ growth in Q2 2025
📉 A minor dip in Q3 followed by recovery in Q4
📈 YoY growth from Q4 2024 to Q4 2025 was over 26%


📽️ Demo Video
🔗 Watch the video demo here
https://drive.google.com/file/d/1po8AnL_IJXD990bQWgalJLcTeoXBuhWZ/view?usp=sharing

👨‍💻 Author
Shaik Manaal
📍 Bengaluru, India
✉️ shaikmanaal67@gmail.com
