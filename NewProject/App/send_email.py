from django.core.cache import cache
from django.core.mail import EmailMultiAlternatives
from django.template import loader

from App.models import User
from homeworkmusic import settings


def send_email(token):
	
	user = User.objects.filter(Token=token).first()
	cache.set('token', user.id, timeout=60)
	subject = '用户激活'
	url = 'http://127.0.0.1:8000/App/activate/?token='+token
	data = {
		'url': url,
		'username': user.U_name,
	}
	template = loader.get_template('JSP.html')
	content = template.render(data)
	from_email = settings.EMAIL_HOST_USER
	recipient_list = [user.U_email, ]
	msg = EmailMultiAlternatives(subject, content, from_email, recipient_list)
	msg.content_subtype = 'html'
	msg.send()

