from flask import Flask,render_template # Khai báo thư viện, đổ cái template vào
app = Flask(__name__) # Tạo một đối tượng Flask và gán cho biến app

@app.route('/')   #Decorator liên kết với hàm index với đường dẫn gốc của úng dụng
def index():      # Khi có yêu cầu nào gửi lên đường dẫn gốc, Flask sẽ gọi hàm index
    return render_template('index.html')

if __name__ == '__main__':#Đoạn code này đảm bảo rằng server của ứng dụng Flask chỉ được khởi chạy khi bạn chạy trực tiếp file Python này.
    app.run(debug=True)   # Cờ debug để khi lỗi sẽ hiện lên thông báo