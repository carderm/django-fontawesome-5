from __future__ import unicode_literals

from django import template
from django.templatetags.static import static
from django.utils.html import format_html, mark_safe, conditional_escape

from .. import Icon
from ..app_settings import get_css, get_js

register = template.Library()


@register.simple_tag
def fa5_icon(*args, **kwargs):
    return Icon(*args, **kwargs).as_html()


@register.simple_tag
def fontawesome_5_static():
    staticfiles = []
    css = get_css()
    js = get_js()

    for css_file in css:
        css_url = css_file if css_file.startswith('http') else static(css_file)
        staticfiles.append(format_html(f'<link href="{css_url}" rel="stylesheet" media="all">'))

    for js_file in js:
        js_url = js_file if js_file.startswith('http') else static(js_file)
        staticfiles.append(format_html(f'<script type="text/javascript" src="{js_url}"></script>'))

    return mark_safe(conditional_escape('\n').join(staticfiles))
