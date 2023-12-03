import streamlit as st
from sqlalchemy import text

list_bank = ['', 'BCA', 'BRI', 'BNI', 'MANDIRI', 'BTN', 'BSI']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://berylathaya2:DONJ9QnABs4q@ep-aged-term-10080143.ap-southeast-1.aws.neon.tech/fp3mbd")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS SCHEDULE (id serial, bank_name varchar, nasabah_name varchar, alamat varchar, rekening varchar, \
                                                       akun varchar, tanggal_pembuatan date, jenis_tabungan varchar, saldo varchar, jumlah_pinjaman text, suku_bunga text);')
    session.execute(query)

st.header('SIMPLE HOSPITAL DATA MANAGEMENT SYS')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM schedule ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO schedule (bank_name, nasabah_name, alamat, rekening, akun, tanggal_pembuatan, jenis_tabungan, saldo, jumlah_pinjaman, suku_bunga) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'', '5':'', '6':'None', '7':'', '8':'', '9':'[]', '10':'[]'})
            session.commit()

    data = conn.query('SELECT * FROM schedule ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        bank_name_lama = result["bank_name"]
        nasabah_name_lama = result["nasabah_name"]
        alamat_lama = result["alamat"]
        rekening_lama = result["rekening"]
        akun_lama = result["akun"]
        tanggal_pembuatan_lama = result["tanggal_pembuatan"]
        jenis_tabungan_lama = result["jenis_tabungan"]
        saldo_lama = result["saldo"]
        jumlah_pinjaman_lama = result["jumlah_pinjaman"]
        suku_bunga_lama = result["suku_bunga"]
        with st.expander(f'a.n. {patient_name_lama}'):
            with st.form(f'data-{id}'):
                bank_name_baru = st.selectbox("bank_name", list_bank, list_bank.index(bank_name_lama))
                nasabah_name_baru = st.selectbox("nasabah_name", list_nasabah, list_nasabah.index(nasabah_name_lama))
                alamat_baru = st.text_input("alamat", alamat_lama)
                rekening_baru = st.text_input("rekening", rekening_lama)
                akun_baru = st.text_input("akun", akun_lama)
                tanggal_pembuatan_baru = st.date_input("tanggal_pembuatan", tanggal_pembuatan_lama)
                jenis_tabungan_baru = st.selectbox("jenis_tabungan", list_jenis, list_jenis.index(jenis_tabungan_lama))
                saldo_baru = st.text_input("saldo", saldo_lama)
                jumlah_pinjaman_baru = st.multiselect("jumlah_pinjaman", ['1000000', '1000000000', '20000000', '5000000', '7000000', '500000000', '100000000'], eval(jumlah_pinjaman_lama))
                suku_bunga_baru = st.multiselect("suku_bunga", ['10%', '5%', '7%', '6%', '8%', '13%', '11%', '2%'], eval(suku_bunga_lama))
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE schedule \
                                          SET bank_name=:1, nasabah_name=:2, alamat=:3, rekening=:4, \
                                          handphone=:5, address=:6, waktu=:7, tanggal=:8 \
                                          WHERE id=:9;')
                            session.execute(query, {'1':bank_name_baru, '2':nasabah_name_baru, '3':alamat_baru,'4':rekening_baru, '5':akun_baru, '6':tanggal_pembuatan_baru, '7':jenis_tabungan_baru, '8':saldo_baru, '9':str(jumlah_pinjaman_baru), '10':str(suku_bunga_baru)})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM schedule WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()