from django.urls import path, include

from m2m import views as m2m_views


urlpatterns = [
    path('', m2m_views.ApiRoot.as_view(), name=m2m_views.ApiRoot.name),
    path('publications/', m2m_views.PublicationList.as_view(), name=m2m_views.PublicationList.name),
    path('publications/<int:pk>/', m2m_views.PublicationDetail.as_view(), name=m2m_views.PublicationDetail.name),
    path('article/', m2m_views.ArticleList.as_view(), name=m2m_views.ArticleList.name),
    path('article/<int:pk>/', m2m_views.ArticleDetail.as_view(), name=m2m_views.ArticleDetail.name),
]
