from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import delete
from unicodedata import category

from app import  db, app

class Category(db.Model): # Model Đây là một lớp cơ sở được cung cấp bởi SQLAlchemy
                          #Khi một class ke thừa db.Model nghĩa là lớp đó đại diện cho 1 bảng.
    id=Column(Integer,primary_key=True, autoincrement=True)
    name=Column(String(50), unique=True, nullable=False)
    products= relationship('Product', backref="category", lazy=True) # Thêm 1 đối tượng catagoty vào pruduct, thằng nào mamy thì lazy=true
class Product(db.Model):
    id=Column(Integer,primary_key=True, autoincrement=True)
    name=Column(String(50),nullable=False)
    description=Column(String(255),nullable=False)
    price=Column(Float,nullable=False)
    image=Column(String(100),nullable=False)
    active=Column(Boolean,default=True)
    category_id=Column(Integer, ForeignKey(Category.id), nullable=False)
if __name__=='__main__':
    with app.app_context():
        db.create_all()
        # c1 =Category(name="Laptop")
        # c2 = Category(name="Mobile")
        # c3 = Category(name="Tablet") # Mỗi đối tượng là một hàng của bảng
        # db.session.add_all([c1,c2,c3])
        # db.session.commit()
        products = [{
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
            "category_id": 1
        }, {
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
            "category_id": 2
        }, {
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 1
        }, {

            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
            "category_id": 1
        }, {
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
            "category_id": 2
        }, {
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 1
        }, {
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
            "category_id": 1
        }, {
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
            "category_id": 2
        }, {
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 1
        }]
        #delete(Category)
        for p in products:
           prod= Product(**p)
           db.session.add(prod)
        db.session.commit()
