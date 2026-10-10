# QuickBite - food delivery site (Django), Swiggy-style

9 fictional restaurants with menus, a cart, checkout and order tracking.

## Run (first time) - Windows PowerShell
    pip install django
    python manage.py migrate
    python manage.py loaddata sample_data
    python manage.py createsuperuser
    python manage.py runserver
- Site:  http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/  (add restaurants and dishes, change order status)
- Tests: python manage.py test

Sample data (restaurants, dishes, prices, ratings) is invented for practice.

## Restaurants
Biryani Bazaar, Dosa Darbar (pure veg), Pizza Piazza, Wok This Way, Burger Barn,
Kebab Kingdom, Sweet Tooth Mithai (pure veg, free delivery), Veggie Vibes (pure veg),
Chettinad Chronicles.

## Features
- Home: search by restaurant, cuisine OR dish name; cuisine chips; pure-veg filter; sort by rating / time / fee
- Restaurant page: menu grouped by section ({% regroup %}), veg / non-veg marks, bestseller tags, ADD and + / - buttons
- Cart (kept in request.session): one restaurant at a time, with a "Replace cart?" page like Swiggy
- Bill: item total + delivery fee + 5% GST; minimum-order check
- Checkout form with validation (10-digit mobile number), then an order is saved to the database
- Order tracking page with 4 steps (a demo button moves it forward; in the admin you can change the status)
- "My Orders" shows only the orders placed from your own browser

## Apps
- restaurants/  models Restaurant, MenuItem; list + detail pages; custom template filter (templatetags/shop_extras.py)
- cart/         cart logic in utils.py; views to add / update / clear; context_processors.py gives {{ cart_count }} to every page
- orders/       models Order, OrderItem; CheckoutForm; checkout, tracking, history
- templates/    base.html + partials/stepper.html (reused in the menu and the cart)

## Ideas to extend it
- Add a coupon code (e.g. WELCOME50 = Rs 50 off) to the cart bill
- Add restaurant reviews (a Review model with a ForeignKey to Restaurant)
- Add user login so orders belong to an account instead of the browser session
