# -*- coding: utf-8 -*-
# nothing here, move on
import logging
from smtplib import SMTPException
from django.db import models
from django.core import mail
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from envelope import settings
from envelope.signals import after_send


logger = logging.getLogger('envelope')


class Appeal(models.Model):
    sender = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=100, verbose_name="Тема", blank=True)
    message = models.TextField(verbose_name="Сообщение")
    date_sent = models.DateTimeField(verbose_name="Дата", auto_now_add=True)

    template_name = 'envelope/email_body.txt'

    def __unicode__(self):
        return self.subject if self.subject else u"Feedback № %s" % self.id

    def send_notification(self):
        message_body = render_to_string(self.get_template_names(), self.get_context())

        try:
            message = mail.EmailMessage(
                subject=settings.SUBJECT_INTRO + self.subject,
                body=message_body,
                from_email=settings.FROM_EMAIL,
                to=settings.EMAIL_RECIPIENTS,
                headers={
                    'Reply-To': self.email
                }
            )
            message.send()
            after_send.send(sender=self.__class__, model_instance=self)
            logger.info(_("Contact form submitted and sent (from: %s)") %
                        self.email)
        except SMTPException:
            logger.exception(_("An error occured while sending the email"))
            return False
        else:
            return True

    def get_context(self):
        """
        Returns context dictionary for the email body template.

        By default, the template has access to all form fields' values
        stored in ``self.cleaned_data``. Override this method to set
        additional template variables.
        """
        return {"appeal": self}

    def get_template_names(self):
        """
        Returns a template_name (or list of template_names) to be used
        for the email message.

        Override to use your own method choosing a template name.
        """
        return self.template_name