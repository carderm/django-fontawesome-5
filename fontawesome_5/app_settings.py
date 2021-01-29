from django.conf import settings


def get_prefix():
    return getattr(settings, 'FONTAWESOME_5_PREFIX', 'fa')


def get_icon_renderer():
    from .renderers import DefaultRenderer, SemanticUIRenderer # pylint: disable=import-outside-toplevel
    renderers = {
        'default': DefaultRenderer,
        'semantic_ui': SemanticUIRenderer
    }
    return renderers[getattr(settings, 'FONTAWESOME_5_RENDERER', 'default')]


def get_fontawesome_5_css():
    return getattr(settings, 'FONTAWESOME_5_CSS', settings.STATIC_URL + 'fontawesome_5/css/all.min.css')


def get_css():
    css = [settings.STATIC_URL + 'fontawesome_5/css/django-fontawesome.css',]
    fontawesome_5_css = get_fontawesome_5_css()
    if fontawesome_5_css:
        css.append(fontawesome_5_css)
    return css


def get_css_admin():
    css = [settings.STATIC_URL +'fontawesome_5/css/django-fontawesome.css', settings.STATIC_URL + 'fontawesome_5/css/all.min.css']
    css_admin = getattr(settings, 'FONTAWESOME_5_CSS_ADMIN', None)
    if css_admin:
        css.append(css_admin)
    return css
