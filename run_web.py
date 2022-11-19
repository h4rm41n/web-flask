# # from flask import Flask, render_template, request, redirect
# # from flaskext.mysql import MySQL
# # import pymysql

# # initial app web
# web = Flask(__name__)

# # # initial mysql database
# # # mysql = MySQL()
# # web.config['MYSQL_DATABASE_HOST'] = 'localhost'
# # web.config['MYSQL_DATABASE_PORT'] = 8889
# # web.config['MYSQL_DATABASE_USER'] = 'root'
# # web.config['MYSQL_DATABASE_PASSWORD'] = 'root'
# # web.config['MYSQL_DATABASE_DB'] = 'kelas_c'
# # # mysql.init_app(web)

# # mysql_1 = MySQL(web, prefix="mysql1", host='localhost', port=8889, user='root', password='root', db='kelas_b', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
# # mysql_2 = MySQL(web, cursorclass=pymysql.cursors.DictCursor)

# # cursor1 = mysql_1.connect().cursor() 
# # cursor2 = mysql_2.connect().cursor()