drop table if exists schedule;
create table schedule (
	id serial,
	bank_name text,
	nasabah_name text,
	alamat text,
	rekening integer,
	akun text,
	tanggal_pembuatan date,
	jenis_tabungan text,
	saldo integer,
	jumlah_pinjaman integer,
	suku_bunga text
);

insert into schedule (bank_name, nasabah_name, alamat, rekening, akun,  tanggal_pembuatan, jenis_tabungan,  saldo, jumlah_pinjaman, suku_bunga) 
values
	('BCA', 'Kevin Caiser', 'Citraland', '117873', 'BCA-73', '2022-12-09', 'Gold', '1000000', '["1000000"]', '["10%"]'),
	('BRI', 'Antonio Moregan', 'Central Park', '172579', 'BRI-79', '2021-11-07', 'Gold', '1340000', '["1000000"]', '["10%"]')
	('BRI', 'Jessica Mirna', 'Puri Galaxy', '163924', 'BRI-24', '2022-04-02', 'Platinum', '67233000', '["100000000", "20000000"]', '["5%", "8%"]')
	('MANDIRI', 'Florencia Agata', 'Pakuwon City', '103850', 'MANDIRI-50', '2022-05-07', 'Gold', '4524247', '["5000000"]', '["13%"]' )
	('BSI', 'Siti Aisya', 'Taman Dayu', '136020', 'BSI-20', '2023-05-08', 'Gold', '6435432', '["7000000"]', '["11%"]' )
	('BNI', 'Lily Gabriela', 'Perumdos blok J ITS', '493613', 'BNI-1', '2023-09-02', 'Gold', '3398909', '["5000000"]', '["13%"]' )
	('BTN', 'Jelian Amberly', 'Gempol Land', '888766', 'BTN-6', '2022-01-17', 'Platinum', '60237963', '["1000000000"]', '["5%"]' )
	('BCA', 'Jeon Jungkook', 'Gebang wetan no 19', '153533', 'BCA-33', '2022-02-03', 'Platinum', '86323000', '["500000000"]', '["6%"]' )
	('MANDIRI', 'Agus Sunaryo', 'Pandaan Regency', '173400', 'MANDIRI-00', '2022-09-04', 'Platinum', '96056000', '["1000000000", "50000000"]', '["2%", "6%"]' )

	;