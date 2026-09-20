# Engineering Monitoring Dashboard

A simple and practical dashboard for monitoring environmental and system conditions in real time.

This project is designed to help users track temperature, humidity, and power usage, then classify each value as NORMAL, WARNING, or CRITICAL.

## English

### Overview
The Engineering Monitoring Dashboard is a Streamlit-based web application that simulates monitoring for engineering systems. It lets users adjust values using sliders and instantly see whether the system is operating safely or needs attention.

### Why this project matters
Modern systems depend on continuous monitoring. This dashboard provides a lightweight and easy-to-understand example of how condition monitoring can be built using Python and Streamlit.

### Features
- Temperature monitoring
- Humidity monitoring
- Power calculation and classification
- Safety alarm system
- Overall system summary page
- Unit tests for validation
- Clean project structure for team collaboration

### Tech Stack
- Python
- Streamlit
- pytest
- Git / GitHub

### Project Structure
```text
Engineering-Monitoring-Dashboard/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── services/
│   ├── __init__.py
│   ├── temperature.py
│   ├── humidity.py
│   ├── power.py
│   └── alarm.py
├── pages/
│   ├── 1_Temperature.py
│   ├── 2_Humidity.py
│   ├── 3_Power.py
│   ├── 4_Safety_Alarm.py
│   └── 5_System_Summary.py
├── tests/
│   ├── test_temperature.py
│   ├── test_humidity.py
│   ├── test_power.py
│   └── test_alarm.py
└── .venv/
```

### Installation
1. Clone the repository.
2. Open a terminal in the project folder.
3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the environment:

Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
source .venv/bin/activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the App
```bash
streamlit run app.py
```

### Run Tests
```bash
pytest -q
```

### Dashboard Modules
- Temperature: tracks thermal conditions
- Humidity: monitors moisture levels
- Power: calculates power from voltage and current
- Safety Alarm: detects warning and critical events
- System Summary: gives an overall system overview

### License
This project is intended for educational and demonstration purposes.

---

## ไทย

### ภาพรวม
Engineering Monitoring Dashboard เป็นแอปพลิเคชันเว็บที่พัฒนาด้วย Streamlit เพื่อจำลองการติดตามสถานะของระบบวิศวกรรม ผู้ใช้สามารถปรับค่าได้ผ่าน Slider และดูผลลัพธ์ทันทีว่าอุปกรณ์อยู่ในสภาวะปลอดภัยหรือจำเป็นต้องได้รับการระวัง

### ทำไมถึงสำคัญ
ระบบสมัยใหม่ต้องมีการตรวจสอบและติดตามสภาพแวดล้อมอย่างต่อเนื่อง Dashboard ตัวนี้ให้ภาพรวมของแนวคิดด้านการตรวจวัดและการแจ้งเตือนแบบง่าย ๆ ที่สามารถพัฒนาต่อได้ในโครงการจริง

### ฟีเจอร์หลัก
- การติดตามอุณหภูมิ
- การติดตามความชื้น
- การคำนวณและจัดระดับกำลังไฟฟ้า
- ระบบแจ้งเตือนความปลอดภัย
- หน้าสรุปสถานะระบบรวม
- การทดสอบด้วย pytest
- โครงสร้างโปรเจกต์ที่เหมาะสำหรับการทำงานเป็นทีม

### เทคโนโลยีที่ใช้
- Python
- Streamlit
- pytest
- Git / GitHub

### โครงสร้างโปรเจกต์
Engineering-Monitoring-Dashboard/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── services/
│   ├── __init__.py
│   ├── temperature.py
│   ├── humidity.py
│   ├── power.py
│   └── alarm.py
├── pages/
│   ├── 1_Temperature.py
│   ├── 2_Humidity.py
│   ├── 3_Power.py
│   ├── 4_Safety_Alarm.py
│   └── 5_System_Summary.py
├── tests/
│   ├── test_temperature.py
│   ├── test_humidity.py
│   ├── test_power.py
│   └── test_alarm.py
└── .venv/
```

### การติดตั้ง
1. Clone โปรเจกต์จาก GitHub
2. เปิด Terminal ในโฟลเดอร์โปรเจกต์
3. สร้าง Virtual Environment:

```bash
python -m venv .venv
```

4. เปิดใช้งาน Environment:

Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
source .venv/bin/activate
```

5. ติดตั้ง dependency:

```bash
pip install -r requirements.txt
```

### รันแอปพลิเคชัน
```bash
streamlit run app.py
```

### รันการทดสอบ
```bash
pytest -q
```

### โมดูลในแอป
- Temperature: ตรวจสอบสภาวะความร้อน
- Humidity: ตรวจสอบระดับความชื้น
- Power: คำนวณกำลังไฟฟ้าจากแรงดันและกระแส
- Safety Alarm: แจ้งเตือนเมื่อเกิด Warning หรือ Critical
- System Summary: สรุปสถานะรวมของระบบ

### ลิขสิทธิ์
โครงการนี้ออกแบบเพื่อการศึกษาและสาธิตการใช้งานจริงของระบบติดตามสถานะอุปกรณ์

---

## Final Summary / สรุปสุดท้าย
This dashboard is designed to make system monitoring easy to understand and visually clear. It helps users explore how engineering conditions can be tracked, classified, and monitored in a modern web interface.

Dashboard นี้ออกแบบมาเพื่อให้ผู้ใช้งานเข้าใจเรื่องการติดตามสถานะระบบได้ง่ายและชัดเจน โดยให้ภาพรวมของวิธีการตรวจสอบและจำแนกสภาวะต่าง ๆ ผ่านอินเทอร์เฟซเว็บที่ใช้งานง่ายและทันสมัย
