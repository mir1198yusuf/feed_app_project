#custom tags/filters to be used in templates
from django import template
from feed.models import PostUser_Upvotes

register = template.Library()

@register.simple_tag(takes_context=True)
def get_pagination_values_3(context):
	"""
	This tag will return three numbers which should be present on pagination links
	according to current page number. will be called when no of pages > 3
	"""
	current_pageno = context.get('page_obj').number
	if current_pageno == 1:
		return (current_pageno, current_pageno+1, current_pageno+2)
	elif current_pageno == context.get('paginator').num_pages:
		return (current_pageno-2, current_pageno-1, current_pageno)
	else:
		return (current_pageno-1, current_pageno, current_pageno+1)

@register.simple_tag
def has_user_upvoted_post(post, user):
	"""
	checks if user has upvotes a post or not
	"""
	ret = None
	if user.is_authenticated:
		try:
			PostUser_Upvotes.objects.get(post=post, upvoted_by=user)
			ret = True
		except PostUser_Upvotes.DoesNotExist:
			ret = False
	else:
		ret = False
	return ret
	
@register.simple_tag
def urltype(value):
	"""
	returns type of url i.e. image, video, or other type
	"""
	if len(value)>4:
		lastfour = value[-4:]
		value = value.lower()
		if lastfour in ('.png','.jpg','.jpeg'):
			return 'image'
		elif lastfour == '.mp4':
			return 'video'
	return 'other'

@register.filter
def red_border_if_error(field):
	"""
	This filter will give red border css class name if form field has errors
	"""
	if field.errors:
		return 'w3-border w3-border-red'
	else:
		return ''