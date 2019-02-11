from django import template
import re
register = template.Library()


@register.filter(name='hash')
def hash(h, key):
	return h[key]

@register.filter(name='dict')
def dict(h):
	return str(dict)

@register.filter(name='keys')
def keys(h):
	return h.keys()

@register.filter(name='widget')
def widget(h):
	start = "<class 'django.forms.widgets."
	end = "'>"
	s = str(type(h.field.widget))
	return s[len(start):-len(end)]

@register.filter(name='widget_readonly')
def widget_readonly(h):
	s = h.field.widget.attrs
	out = False
	if "readonly" in s.keys():
		out = out or s["readonly"]
	return out