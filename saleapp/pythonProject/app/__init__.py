from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy #Khai báo thư viện
app = Flask(__name__) # Tạo một đối tượng Flask và gán cho biến app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ='mysql+pymysql://root:%s@localhost/saledb' % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"]= 4
db=SQLAlchemy(app=app) # Điều này khởi tạo SQLAlchemy và liên kết nó với ứng dụng Flask
