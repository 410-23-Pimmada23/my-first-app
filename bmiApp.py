import streamlit as st

#ส่วนที่1 หัวข้อหน้าเว็บ ( Title สีแดง)
st.markdown("# :red[🏃 🏋️ คำนวนค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

#ส่วนที่2 สร้างช่องรับค่าน้ำหนัก และ ส่วนสูง
wight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):", min_value=1.0, value=1.0)
height_cm = st.number_input("กรอกน้ส่วนสูงของคุณ (เซนติเมตร):", min_value=1.0, value=1.0)

#ส่วนที่3 สร้างปุ่มกดคำนวณ
if st.button("คำนวณค่า BMI 🚨"):
   # แปลงส่วนสูงจาก cm เป็น เมตร แล้วคำนวน BMI
   height_m = height_cm / 100
   bmi = weight / (height_m ** 2 )
   
    
  
   
  
