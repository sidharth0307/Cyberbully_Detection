from django.contrib import admin
from encryptapp.models import police_station
from encryptapp.models import FAQ
from encryptapp.models import Laws
from encryptapp.models import Terms
from encryptapp.models import cybersecurity_laws
from encryptapp.models import userregister
from encryptapp.models import contact_us
from encryptapp.models import review
from encryptapp.models import help_support

# Register your models here.
admin.site.register(police_station)
admin.site.register(FAQ)
admin.site.register(Laws)
admin.site.register(Terms)
admin.site.register(cybersecurity_laws)
admin.site.register(userregister)
admin.site.register(contact_us)
admin.site.register(review)
admin.site.register(help_support)