from flask import Flask, render_template, request
from flaskext.mysql import MySQL

# initial app web
web = Flask(__name__)

# initial mysql database
mysql = MySQL()
web.config['MYSQL_DATABASE_HOST'] = 'localhost'
web.config['MYSQL_DATABASE_PORT'] = 8889
web.config['MYSQL_DATABASE_USER'] = 'root'
web.config['MYSQL_DATABASE_PASSWORD'] = 'root'
web.config['MYSQL_DATABASE_DB'] = 'kelas_c'
mysql.init_app(web)
conn = mysql.connect()


@web.route('/')
def Home():
    return render_template('home.html')

@web.route('/mahasiswa')
def ListMahasiswa():
    cursor = conn.cursor()
    query = ("SELECT * FROM tb_mahasiswa")
    cursor.execute(query)
    result = cursor.fetchall()
    
    return render_template('list_mhs.html', data=result)

@web.route('/form', methods=['GET', 'POST'])
def Form():
    if request.method == 'POST':
        data = request.form
        nama = data['nama']
        nim = data['nim']
        alamat = data['alamat']

        cursor = conn.cursor()
        # INSERT INTO `tb_mahasiswa` (`id`, `nama`, `nim`, `alamat`) VALUES (NULL, 'Ilyasin', '20.48.55.001', 'Anjani');
        sql = f"INSERT INTO tb_mahasiswa (nama, nim, alamat) VALUES('{nama}', '{nim}', '{alamat}')"
        query = (sql)
        cursor.execute(query)
    
    return render_template('form.html')


@web.route('/hapus')
def HapusMhs():
    return 'TEST HAPUS DATA'

if __name__ == '__main__':
    web.run()