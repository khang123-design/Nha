from app.models import Category, Product

def load_categories():
    return Category.query.order_by('id').all()


def load_products(cate_id=None): #lọc dữ liệu,  Nếu có ID danh mục, thì lọc các sản phẩm dựa trên điều kiện category_id bằng với ID danh mục đã cho.
    query = Product.query
    if cate_id:
        query = query.filter(Product.category_id == cate_id)

    return query.all()

