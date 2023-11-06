from django.contrib import admin

# Register your models here.
from .models import registration
admin.site.register(registration)


from .models import contact
admin.site.register(contact)


from .models import c_job
admin.site.register(c_job)

from .models import sp_registration
admin.site.register(sp_registration)

from .models import sp_news
admin.site.register(sp_news)

from .models import quiz
admin.site.register(quiz)

from .models import s_payment
admin.site.register(s_payment)
