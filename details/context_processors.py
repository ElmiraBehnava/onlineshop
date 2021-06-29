from shop.models import Category

def show_categories(request):
    product_categories = Category.objects.all()
    return {'categories':product_categories}