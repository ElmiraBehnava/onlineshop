from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Comment
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('-created')
    countof = Product.objects.all().count()
    new_product = Product.objects.all()[:3]
    if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)

    object_list = Product.objects.all()
    paginator = Paginator(products, 8) # number of show products in each page
    page_number = request.GET.get('page')
    products_of_each_page = paginator.get_page(page_number) # page_obj = products in each page
    return render(request, 'shop/product_list.html', {'category': category, 'categories': categories, 'products': products_of_each_page, 'countof': countof, 'new_product':new_product})



def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id, slug=slug, available=True)
    comments = product.comments.filter(active=True)
    cart_product_form = CartAddProductForm()
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()


    return render(request, 'shop/product_detail.html', {'product': product, 'comments': comments, 'cart_product_form': cart_product_form, 'new_comment': new_comment,'comment_form': comment_form} )