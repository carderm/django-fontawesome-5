from django.utils.html import mark_safe
from .app_settings import get_prefix


prefix = get_prefix()


class FontawesomeRenderer:
    classes = {
        'border': 'fa-border',
        'class': '{}',
        'fixed_width': 'fa-fw',
        'flip': 'fa-flip-{}',
        'li': 'fa-li',
        'pull': 'fa-pull-{}',
        'pulse': 'fa-pulse',
        'rotate': 'fa-rotate-{}',
        'size': '{}',
        'spin': 'fa-spin',
    }

    attrs = {
        'title': 'title="{}"',
        'color': 'style="color:{};"',
    }

    def render(self, Icon):
        if Icon.name:
            classes = []
            attrs = []
            for key, value in Icon.kwargs.items():
                if key in self.classes:
                    classes.append(self.classes[key].format(value))
                elif key in self.attrs:
                    attrs.append(self.attrs[key].format(value))

            return mark_safe('<i class="{style_prefix} {prefix}-{name} {classes}" {attrs}></i>'.format(
                style_prefix=Icon.style_prefix,
                prefix=prefix,
                name=Icon.name,
                classes=" ".join(classes),
                attrs=" ".join(attrs)))
        return ''

