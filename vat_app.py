import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
vat = price * 0.07
net_price = price - vat
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.divider()
st.write("นางสาวพิมพ์มาดา ขัดขจร เลขที่ 23  ม.4/10")
