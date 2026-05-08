import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="ระบบตรวจสอบรายชื่อ", page_icon="📂", layout="wide")

st.title("📂 ระบบตรวจสอบรายชื่อนักเรียน")
st.write("กรุณาอัปโหลดไฟล์ CSV เพื่อเริ่มต้นใช้งาน")

# ส่วนปุ่มอัปโหลดไฟล์ (นี่คือส่วนที่จะทำให้หน้าเว็บเปลี่ยนไปตามรูปที่คุณต้องการ)
uploaded_file = st.file_uploader("เลือกไฟล์ CSV (เช่น users_lpp9.csv)", type=["csv"])

if uploaded_file is not None:
    try:
        # ลองอ่านไฟล์ด้วย UTF-8 ถ้าไม่ได้ให้ลอง TIS-620
        try:
            df = pd.read_csv(uploaded_file, encoding='utf-8')
        except:
            df = pd.read_csv(uploaded_file, encoding='tis-620')

        st.success("เชื่อมต่อข้อมูลสำเร็จ!")

        # ส่วนการค้นหา
        search = st.text_input("🔍 ค้นหาชื่อ หรือ อีเมล...")
        
        if search:
            mask = df.apply(lambda x: x.astype(str).str.contains(search, case=False).any(), axis=1)
            st.dataframe(df[mask], use_container_width=True, hide_index=True)
        else:
            st.dataframe(df, use_container_width=True, hide_index=True)

    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {e}")
else:
    st.info("รอการอัปโหลดไฟล์... กรุณากดปุ่ม Browse files ด้านบน")
