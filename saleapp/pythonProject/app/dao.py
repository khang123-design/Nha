from keyword import kwlist

from app.models import Category, Product

def load_categories():
    return Category.query.order_by('id').all() #Truy vấn bảng Category với id tăng dần


def load_products(cate_id=None, kw=None): #lọc dữ liệu,  Nếu có ID danh mục, thì lọc các sản phẩm dựa trên điều kiện category_id bằng với ID danh mục đã cho.
    query = Product.query
    if cate_id: #Xét coi có nhập vào cate_id hay ko
        query = query.filter(Product.category_id == cate_id) #fiilter để thêm điều kiện lọc các sản phẩm có trường la category_id
    if kw:
        kwlist = kw.split()  # Tách chuỗi kw thành danh sách các từ
        for word in kwlist:
            query = query.filter(Product.name.contains(word))

    return query.all() #Truy vấn các dữ liệu.
def get_product_by_id(product_id):
    return Product.query.get(product_id)  #Trả về một đối tượng
