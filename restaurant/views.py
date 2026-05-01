from django.shortcuts import render,redirect
from .models import Menu, Table, Order

def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'restaurant/menu_list.html', {'menus': menus})


def table_list(request):
    tables = Table.objects.all()
    return render(request, 'restaurant/table_list.html', {'tables': tables})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'restaurant/order_list.html', {'orders': orders})
from .models import Menu, Table, Order

def home(request):
    menus_count = Menu.objects.count()
    tables_count = Table.objects.count()
    orders = Order.objects.all()

    total_revenue = sum(order.total_price() for order in orders)

    return render(request, 'restaurant/home.html', {
        'menus_count': menus_count,
        'tables_count': tables_count,
        'orders_count': orders.count(),
        'revenue': total_revenue
    })

def add_order(request):
    if request.method == "POST":
        table_id = request.POST.get("table")
        items_ids = request.POST.getlist("items")

        if table_id:  # حماية
            table = Table.objects.get(id=table_id)
            order = Order.objects.create(table=table)

            order.items.set(items_ids)
            order.save()

        return redirect('order_list')

    tables = Table.objects.all()
    menus = Menu.objects.all()

    return render(request, 'restaurant/add_order.html', {
        'tables': tables,
        'menus': menus
    })