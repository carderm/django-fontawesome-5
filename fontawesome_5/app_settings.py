from django.conf import settings


def get_prefix():
    return getattr(settings, 'FONTAWESOME_5_PREFIX', 'fa')


def get_js():
    js = getattr(settings, 'FONTAWESOME_5_JS', 'fontawesome_5/js/all.min.js')
    if type(js) == str:
        js = [js]
    return js


def get_css():
    css = getattr(settings, 'FONTAWESOME_5_CSS', 'fontawesome_5/css/all.min.css')
    if type(css) == str:
        css = [css]
    return css


def get_css_admin():
    css = ['fontawesome_5/css/django-fontawesome.css',
           'fontawesome_5/css/all.min.css']
    css_admin = getattr(settings, 'FONTAWESOME_5_CSS_ADMIN', None)
    if css_admin:
        if type(css_admin) == str:
            css.append(css_admin)
        else:
            css += css_admin
    return css


def get_js_admin():
    js = ['fontawesome_5/js/django-fontawesome.js',]
    js_admin = getattr(settings, 'FONTAWESOME_5_JS_ADMIN', None)
    if js_admin:
        if type(js_admin) == str:
            js.append(js_admin)
        else:
            js += js_admin
    return js
