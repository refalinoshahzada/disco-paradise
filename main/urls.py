from django.urls import path
from main.views import show_main, create_album_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user
from main.views import edit_album, delete_album, add_album_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-album-entry', create_album_entry, name='create_album_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-album/<uuid:id>', edit_album, name='edit_album'),
    path('delete-album/<uuid:id>', delete_album, name='delete_album'),
    path('add-album-entry-ajax/', add_album_entry_ajax, name='add_album_entry_ajax'),
]