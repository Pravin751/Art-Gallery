from django.contrib import admin
from  app.models import register33
from  app.models import ArtistAccount
from  app.models import Category
from  app.models import cart
from  app.models import Order
from app.models import Photo
from app.models import Customphoto
from app.models import Selleraccount

admin.site.site_header = 'Art Gallery Administration'
admin.site.site_title = 'Art Gallery Admini Portal'
admin.site.index_title = 'Welcome to Art Gallery '

admin.site.register(register33)
admin.site.register(ArtistAccount)
admin.site.register(Category)
admin.site.register(cart)
admin.site.register(Order)
admin.site.register(Photo)
admin.site.register(Customphoto)
admin.site.register(Selleraccount)


    

