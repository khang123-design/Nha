from flask import Flask
from flask_sqlalchemy import SQLAlchemy #Khai báo thư viện
app = Flask(__name__) # Tạo một đối tượng Flask và gán cho biến app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:123456@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db=SQLAlchemy(app=app) # Điều này khởi tạo SQLAlchemy và liên kết nó với ứng dụng Flask
