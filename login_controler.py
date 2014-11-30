# -*- coding:utf-8 -*-

from base_controler import BaseHandler
from settings import FACTORY

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html', errormessage='', next=self.get_argument("next","/posts/"))

    def post(self):
        getusername = self.get_argument("username")
        getpassword = self.get_argument("password")
        dao = FACTORY.getUserDao() 
        if dao.check_permission(getusername, getpassword):
            self.set_secure_cookie("user", getusername, expires_days=None)
            self.redirect(self.get_argument("next", "/"))
        else:
            self.render(
                'login.html',
                errormessage="Usuário ou senha incorretos!",
                next=self.get_argument("next","/")
            )


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", "/posts/"))

