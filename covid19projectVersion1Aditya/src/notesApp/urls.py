from django.urls import include,path
from .views import (
    welcome,
    listNotes,
    addNotes,
    loginNotesApp,
    modifyNotes,
    deleteNotes,
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('details/delete/<int:id>', deleteNotes,name='deleteNotes'),
    path('details/modify/<int:id>', modifyNotes,name='modifyNotes'),
    path('', loginNotesApp,name='loginNotesApp'),
    path('details/add/', addNotes,name='addNotes'),
    path('details/', listNotes,name='listNotes'),
    path('welcome/', welcome,name='welcome'),
]
urlpatterns+=staticfiles_urlpatterns()