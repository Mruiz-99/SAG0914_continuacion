import os
import pathlib

import yagmail
from dataclasses import dataclass
from string import Template

_USER = os.getenv('EMAIL_USER')
_PASS = os.getenv('EMAIL_PASS')
_FROM = os.getenv('EMAIL_FROM')

templates = {
    'notification': './templates/notification.html',
    'resetPassword': './templates/resetPassword.html',
    'confirmEmail': './templates/confirmEmail.html',
    'jobInterview': './templates/jobInterview.html',
}


@dataclass
class Email:
    to: str
    subject: str
    attachments: list
    message: str
    template: str
    title: str
    html: str
    data: dict or None
    __yag = yagmail.SMTP({_USER: _FROM}, _PASS)

    def __content(self):
        if not self.html:
            with open(templates.get(self.template)) as f:
                t = Template(f.read())
                content = t.substitute(**self.data, title=self.title, message=self.message) if self.data \
                    else t.substitute(title=self.title, message=self.message)
        else:
            content = self.html
        print(self.data)
        return content

    def send_notification(self):
        try:
            self.__yag.send(to=self.to, subject=self.subject, contents=self.__content(), attachments=self.attachments)
            return None
        except Exception as err:
            print(f'ERROR TO SEND EMAIL: {err}')
            return err.__str__()
