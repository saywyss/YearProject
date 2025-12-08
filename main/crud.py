import main.models as models

def get_products():
    return models.Product.objects.all()

def get_product_by_id(product_id):
    return models.Product.objects.get(id=product_id)

# create
def create_product(name, price, category, description, count):
    product = models.Product(
        name=name,
        price=price,
        category=category,
        description=description,
        count=count
    )
    product.save()
    return product

# update
def update_product(product_id, name = None, price = None, category = None, description = None, count = None):
    product = models.Product.objects.get(id=product_id)
    
    if name is not None:
        product.name = name
        
    if price is not None:
        product.price = price
        
    if category is not None:
        product.category = category
        
    if description is not None:
        product.description = description
        
    if count is not None:
        product.count = count
        
    product.save()
    return product

# delete
def delete_product(product_id):
    product = models.Product.objects.get(id=product_id)
    return product.delete()


# user orders
def get_user_orders(user):
    return models.Order.objects.filter(user=user)

def search_products_by_name(name):
    return models.Product.objects.filter(name__icontains=name)

def get_products_by_category(category):
    return models.Product.objects.filter(category=category)

# .all() - получить ВСЕ
# .filter(user=request.user) - получить ВСЕ заказы пользователя
# .get(user=request.user) - получить 1 заказ пользователя