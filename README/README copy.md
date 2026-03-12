# `Predictive maintenance`

Model: LightGBM + Optuna + Feature Engineering

[ รายละเอียด Project ]
Project สำหรับวิเคราะห์และพยากรณ์ค่าความสั่นสะเทือน (Vibration) จากข้อมูลในไฟล์ .txt
โดยใช้ Machine Learning (LightGBM) ร่วมกับการปรับจูนพารามิเตอร์อัตโนมัติ (Optuna)
และการวิเคราะห์ทางสถิติเพื่อหาแนวโน้ม (Trend Analysis)

[ การติดตั้ง (Dependencies) ]
กรุณาติดตั้ง Library ที่จำเป็นก่อนใช้งาน:

pip install lightgbm optuna scikit-learn pandas numpy matplotlib joblib

[ โครงสร้างข้อมูลที่รองรับ ]

ไฟล์นามสกุล .txt

ข้อมูลควรมีการจัดรูปแบบที่สามารถแยกแยะ Header และ Value ได้ (ตามฟังก์ชัน parse_vibration_file)

[ วิธีใช้งาน ]

รันผ่าน Terminal/Command Prompt:
python train.py

เลือกเมนูการทำงาน:
[1] วิเคราะห์ไฟล์ .txt รายไฟล์ (ระบุ Path ของไฟล์)
[2] วิเคราะห์ทั้งโฟลเดอร์ (ระบุ Path ของโฟลเดอร์ที่มีไฟล์ .txt หลายไฟล์)
[3] บันทึกผลสรุป (Summary Report)
[q] ออกจากโปรแกรม

[ ฟีเจอร์เด่น ]

Feature Engineering: สร้างข้อมูล Lag (20), Rolling Statistics (10, 20, 50), และ FFT

Optimization: ค้นหาค่า Hyperparameter ที่ดีที่สุดอัตโนมัติด้วย Optuna (50 Trials)

Validation: ใช้ TimeSeriesSplit เพื่อป้องกันการ Overfit ของข้อมูลอนุกรมเวลา

Output: แสดงผล RMSE, MAE และกราฟเปรียบเทียบค่าจริง/ค่าพยากรณ์ พร้อมวิเคราะห์ Trend

[ การตั้งค่า (Configuration) ]
สามารถปรับแต่งค่าได้ในส่วนต้นของไฟล์ train.py:

N_LAGS        = 20

ROLLING_WINS  = [10, 20, 50]

OPTUNA_TRIALS = 50

TEST_RATIO    = 0.2 (สัดส่วนข้อมูลทดสอบ 20%)
