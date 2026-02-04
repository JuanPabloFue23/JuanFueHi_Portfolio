# Air Quality Guardian 🛡️

A real-time monitoring tool designed to track and analyze urban air quality using the **OpenAQ API**. This project demonstrates professional API integration by fetching live environmental data and processing it into structured formats.

## ✨ Key Features
* **Live API Integration:** Connects to OpenAQ to fetch real-time PM2.5 levels.
* **Data Analysis:** Automatically evaluates air quality status based on health standards.
* **Persistence:** Logs every check into a local `air_quality_log.csv` for historical tracking.

## 🛠️ Technologies
* Python 3.x 🐍
* Requests library (API handling)
* CSV module (Data persistence)

## 🚀 How to Run
1. **Clone the repository:**
   `git clone https://github.com/JuanPabloFue23/JuanFueHi_Portfolio.git`
2. **Navigate to the project:**
   `cd projects/air-quality-project`
3. **Install dependencies:**
   `pip install -r requirements.txt`
4. **Run the guardian:**
   `python main.py`