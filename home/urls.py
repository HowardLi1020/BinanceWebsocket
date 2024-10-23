from django.urls import path
from . import views  # 導入 views 模塊

urlpatterns = [
    path('', views.index, name='index'),  # 設定根路由對應到 index 視圖
]