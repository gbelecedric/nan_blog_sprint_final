
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

from rest_framework.routers import DefaultRouter

from .apiviews import CategorieViewSet, TagViewSet, ArticleViewSet, CommentaireViewSet, ReplyViewSet, LikeViewSet, searchViewSet, VueViewSet, Visitor_Infos_userViewSet, MessageViewSet, NewsletterViewSet,  LinkViewSet, InfoViewSet, instagram_feedViewSet, FooterViewSet, BackgroundViewSet, HomeViewSet, MembreViewSet


router = DefaultRouter()
router.register('categorie', CategorieViewSet, base_name='categorie')
router.register('tag', TagViewSet, base_name='tag')
router.register('article', ArticleViewSet, base_name='article')
router.register('commentaire', CommentaireViewSet, base_name='commentaire')
router.register('reply', ReplyViewSet, base_name='reply')
router.register('like', LikeViewSet, base_name='Like')
router.register('search', searchViewSet, base_name='search')
router.register('vue', VueViewSet, base_name='VueViewSet')
router.register('infovisiteur', Visitor_Infos_userViewSet, base_name='infovisiteur')
router.register('message', MessageViewSet, base_name='message')
router.register('newsletter', NewsletterViewSet, base_name='newsletter')

router.register('link', LinkViewSet, base_name='link')
router.register('info', InfoViewSet, base_name='info')
router.register('instagram', instagram_feedViewSet, base_name='instagram')
router.register('foot', FooterViewSet, base_name='foot')
router.register('back', BackgroundViewSet, base_name='back')
router.register('home', HomeViewSet, base_name='home')
router.register('membre', MembreViewSet, base_name='membre')

urlpatterns = [
 
]

urlpatterns += router.urls
