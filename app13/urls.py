from django.urls import path
from.views import display_new_form as idx1
from.views import receive_new_form as idx2
from.views import display_search_form as idx3
from.views import search_person as idx4
from.views import display_update_search_form as idx5
from.views import display_update_form as idx6
from.views import receive_update as idx7
from.views import search_delete_form as idx8
from.views import display_delete_form as idx9
from.views import delete as idx10
from.views import display_all as idx11
from.views import display_insert_form as idx12
from.views import insert as idx13
from.views import home as idx

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('display_newform', idx1),
    path('receive_newform', idx2),
    path('display_search_form', idx3),
    path('search_person', idx4),
    path('display_update_search_form', idx5),
    path('display_update_form', idx6),
    path('receive_update', idx7),
    path('delete_search_form', idx8),
    path('display_delete_form', idx9),
    path('delete', idx10),
    path('display_all', idx11),
    path('display_insert_form', idx12),
    path('insert', idx13),
    path('', idx),
]
