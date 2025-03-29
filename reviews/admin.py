from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review)



class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date' #useful
    list_filter = ('publisher','publication_date')
    search_fields = ('title','isbn__exact','publisher__name') # 2 underscore if we want to use foreign relations
    # exact unsures no partial checking
    list_display = ('title','isbn13','has_isbn')#custom list possible just gotta be creative enough
    def has_isbn(Self,obj):
        return bool (obj.isbn)
    def isbn13(self,obj):
        return "{} - {} - {} - {} - {}".format(obj.isbn[0:3],obj.isbn[3:4],obj.isbn[4:6],obj.isbn[6:12],obj.isbn[12:13])


#refer this whenever registering the new books

admin.site.register(Book,BookAdmin) #there was an error here trying to register book twice had to remove one line from above


def initialled_name(obj):
    initials = "".join([name[0] for name in obj.first_names.split(" ")])
    return "{}, {}".format(obj.last_names, initials)

class ContributorAdmin(admin.ModelAdmin):
    list_display = ("last_names", "first_names")
    list_filter = ("last_names",)
    search_fields = ("last_names__startswith", "first_names")

class ReviewAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {"fields": ("creator", "book")}),
        ("Review content", {"fields": ("content", "rating")}),
    )

admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)  # here book was registered(removed)
admin.site.register(BookContributor)
admin.site.register(Review)