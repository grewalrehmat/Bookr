from django.contrib import admin
class BookrAdmin(admin.AdminSite):
    title_header='Bookr Header'
    site_header = 'Bookr Administration'
    index_title = 'Bookr site admin'
    login_template = 'reviews/loginadmin.html'
