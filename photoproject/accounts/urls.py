from django.urls import path
# viewsモジュールをインポート
from . import views
# viewsをインポートしてauth_viewという記名で利用する
from django.contrib.auth import views as auth_views

# URLパターンを逆引きできるように名前を付ける
app_name = 'accounts'

urlpatterns = [
    path('signup/',
         views.SignUpView.as_view(),
         name='signup'),
    
    path('signup_success/',
         views.SignUpSuccessView.as_view(),
         name='signup_success'),

    path('login/',
         # ログイン用のテンプレート(フォーム)をレンダリング
         auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='login'
         ),
    
    path('logout/',
         auth_views.LogoutView.as_view(template_name='accounts/logout.html'),
         name='logout'
         ),
]