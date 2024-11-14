from sqlalchemy import  Column,Integer, String, Float
from app import  db, app

class Category(db.Model): # Model Đây là một lớp cơ sở được cung cấp bởi SQLAlchemy
                          #Khi một class ke thừa db.Model nghĩa là lớp đó đại diện cho 1 bảng.
    id=Column(Integer,primary_key=True, autoincrement=True)
    name=Column(String(50), unique=True, nullable=False)

if __name__=='__main__':
    with app.app_context():
        #db.create_all()
        c1 =Category(name="Laptop")
        c2 = Category(name="Mobile")
        c3 = Category(name="Tablet") # Mỗi đối tượng là một hàng của bảng
        db.session.add_all([c1,c2,c3])
        db.session.commit()
