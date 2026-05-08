import streamlit as st
import pandas as pd

st.set_page_config(page_title="ระบบตรวจสอบรายชื่อ", layout="wide")

st.title("📂 ระบบตรวจสอบรายชื่อนักเรียน")

# สร้างปุ่มสำหรับอัปโหลดไฟล์
uploaded_file = st.file_uploader("เลือกไฟล์ CSV (เช่น users_lpp9.csv)", type=["csv"])

if uploaded_file is not None:
    try:
        # อ่านไฟล์ที่เลือกมา
        df = pd.read_csv(uploaded_file, encoding='utf-8')
        st.success("เชื่อมต่อข้อมูลสำเร็จ!")
        
        # ช่องค้นหา
        search = st.text_input("🔍 ค้นหาชื่อ หรือ อีเมล...")
        if search:
            mask = df.apply(lambda x: x.astype(str).str.contains(search, case=False).any(), axis=1)
            st.dataframe(df[mask], use_container_width=True, hide_index=True)
        else:
            st.dataframe(df, use_container_width=True, hide_index=True)
    except Exception as e:
        # ถ้า Error เรื่องภาษาไทย ให้ลองอ่านอีกแบบ
        try:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file, encoding='tis-620')
            st.success("เชื่อมต่อข้อมูลสำเร็จ (TIS-620)!")
            st.dataframe(df, use_container_width=True, hide_index=True)
        except:
            st.error(f"ไม่สามารถอ่านไฟล์ได้: {e}")
else:
    st.info("กรุณาอัปโหลดไฟล์ CSV เพื่อเริ่มต้น")
