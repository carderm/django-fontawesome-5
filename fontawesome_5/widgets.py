from __future__ import absolute_import

from django import forms

from fontawesome_5.app_settings import get_js_admin, get_css_admin


class IconWidget(forms.Select):
    template_name = 'fontawesome_5/select_icon.html'

    class Media:

        js = get_js_admin()

        css = {
            'all': get_css_admin()
        }
