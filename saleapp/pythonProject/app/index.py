from flask import render_template, request # Khai báo thư viện, đổ cái template vào
import dao
from app import app


@app.route('/')   #Decorator liên kết với hàm index với đường dẫn gốc của úng dụng
def index():      # Khi có yêu cầu nào gửi lên đường dẫn gốc, Flask sẽ gọi hàm index
    cates=dao.load_categories() #Gọi hàm load_catagories trong thư mục py và gán dữ liệu cho nó
    cate_id=request.args.get('category_id')
    prods= dao.load_products(cate_id=cate_id)
    return render_template('index.html', categories=cates, products=prods) #Phải tạo 1 biến để gán vì nếu ko có sẽ gây khó khăn cho bên html

if __name__ == '__main__':#Đoạn code này đảm bảo rằng server của ứng dụng Flask chỉ được khởi chạy khi bạn chạy trực tiếp file Python này.
    app.run(debug=True)   # Cờ debug để khi lỗi sẽ hiện lên thông báo