# -*- coding: utf-8 -*-
from django import forms
from envelope.models import Appeal


class ContactForm(forms.ModelForm):
    """
    Base contact form class.

    The following form attributes can be overridden when creating the
    form or in a subclass. If you need more flexibility, you can instead
    override the associated methods such as `get_from_email()` (see below).

    ``subject_intro``
        Prefix used to create the subject line. Default is
        ``settings.ENVELOPE_SUBJECT_INTRO``.

    ``from_email``
        Used in the email from. Defaults to
        ``settings.ENVELOPE_FROM_EMAIL``.

    ``email_recipients``
        List of email addresses to send the email to. Defaults to
        ``settings.ENVELOPE_EMAIL_RECIPIENTS``.

    ``template_name``
        Template used to render the email message. Defaults to
        ``envelope/email_body.txt``.

    """
    class Meta:
        model = Appeal