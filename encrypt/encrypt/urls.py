"""
URL configuration for encrypt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from encryptapp import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_header="Welcome to admin panel"
admin.site.site_title="my title"
admin.site.index_title="Welcome to page"


urlpatterns = [
    path("admin/", admin.site.urls),
     path("footer", views.footer),
     path("contactus", views.contactus, name="contactus"),
     path("registerform1", views.registerform1, name="registerform1"),
     path("header", views.header),
     path("", views.homepage,name="homepage"),
      path("registerform", views.registerform,name="registerform"),
      # path("registerform1", views.registerform1,name="registerform1"),
      path("login", views.login,name="login"),
      path("logout", views.logout,name="logout"),
      path("base", views.base),
      path("allfaq", views.allfaq,name="allfaq"),
      path("allpolicestation", views.allpolicestation, name="allpolicestation"),
      path("alllaws", views.alllaws,name="alllaws"),
      path("allterms", views.allterms,name="allterms"),
      path("allcybersecuritylaws", views.allcybersecuritylaws,name="allcybersecuritylaws"),
       path("sidear1", views.sidear1),
      path("changepass", views.changepass, name="changepass"),
       path("review", views.myreview, name="review"),
       path("help_support", views.help_support1,name="help_support"),
       path("userprofile", views.userprofile,name="userprofile"),
        path("editprofile", views.editprofile,name="editprofile"),
        path("forgotpass", views.forgotpass,name="forgotpass"),
        path("TTS", views.TTS,name="TTS"),
        path("STT", views.STT,name="STT"),
        path("WC", views.WC,name="WC"),
        path("sentiment", views.sentiment,name="sentiment"),
        path("langdetector", views.langdetector,name="detect"),
        path("langconverter", views.langconverter,name="convert"),
        path("linguistic", views.linguistic,name="analyse"),
         path("abusive", views.abusive,name="abusive"),
         path("news", views.news,name="news"),
         path("aboutus", views.aboutus,name="aboutus"),




]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)