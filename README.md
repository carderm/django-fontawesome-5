# django-fontawesome-5

A utility for using icons in models, forms, and templates.
Does support Django 3.0, which *django-fontawesome* will not.

![Clip of dropdown](https://github.com/BenjjinF/django-fontawesome/blob/master/docs/images/django-fontawesome-5.gif)

## Latest Changes

 - Updated Fontawesome to 5.15.3
 - Updated for use with Font Awesome 5 ONLY
 - Static files made all links relative to static_url using Django Static methods
 - Removed Semantic UI renderers - this is a Fontawesome plugin...
 - Added JS for Admin and refactored URLs to allow absolute and Static relative  

## Migration guide from django-fontawesome

1. Remove all occurences of     {% fontawesome_stylesheet %}
1. Replace {% load fontawesome %} with {% load fontawesome_5 %}
1. Replace '{% fontawesome_icon' with '{% fa5_icon'
1. Replace iconnames, for example "bell" needs to be replaced with "bell fas" and "linedin-square" with "linkedin fab"

## Installation / Usage

    pipenv install django-fontawesome-5

Add 'fontawesome_5' to your installed `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        'fontawesome_5',
    )


Import and use `IconField`:
    
    from fontawesome_5.fields import IconField

    class Category(models.Model):
        ...
        icon = IconField()


Include Static Files

    {% load fontawesome_5 %}

    <head>
      {% fontawesome_5_static %} 
      ...
    </head>

## Settings

You can configure django-fontawesome to use another release/source/cdn by specifying the URLs below. 
These can be absolute `https://cdn....` or relative to Django static `fontawsome_5/file.css` ::

    FONTAWESOME_5_CSS = URL or [URLS,] or None
        default: 'fontawesome_5/css/django-fontawesome.css'
    FONTAWESOME_5_JS = URL or [URLS,] or None
        default: 'fontawesome_5/css/django-fontawesome.css'
    FONTAWESOME_5_CSS_ADMIN = URL or [URLS,] or None
        default: None
    FONTAWESOME_5_JS_ADMIN = URL or [URLS,] or None
        default: None
    FONTAWESOME_5_PREFIX = 'custom_prefix'
        default: 'fa'

## Rendering

You can do a simple render  in your template like this:
    
    {% for category in categories.all %}
        {% if category.icon %}
            {{ category.icon.as_html }}
        {% endif %}
    {% endfor %}

### Default Renderer

Or you can use the `{% fa5_icon %}` template tag.

    {% fa5_icon 'github' 'fab' %}

Positional arguments: `icon` (required), `style_prefix` (default: 'fas')

#### Key word arguments:
  - class `extra custom classes`
  - color `CSS Color Names`
  - border `boolean`
  - fixed_width `boolean`
  - flip
    - `horizontal`
    - `vertical`
  - li `boolean`
  - pull
   - `left`
   - `right`
  - pulse `boolean`
  - rotate `integer`
  - size 
     - `fa-xs`
     - `fa-sm`
     - `fa-lg`
     - `fa-2x`
     - `fa-3x`
     - `fa-5x`
     - `fa-7x`
     - `fa-10x`
  - spin `boolean`
  - title `string`

## Credit

  - https://github.com/redouane for the original
  - https://github.com/BenjjinF for the current Fontawesome version 5
  - https://github.com/aatrubilin for current fork/fixes with manifest files


