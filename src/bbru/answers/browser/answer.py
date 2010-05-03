# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Предложить ответ.
"""

from zope.event import notify
from zope.container.interfaces import INameChooser
from zope.lifecycleevent import ObjectCreatedEvent
from bbru.answers import QuestionAnswer

class Ajax:

    def __call__(self):
        body = self.request.get('body')

        if body:
            ob = QuestionAnswer()
            ob.body = body
            notify(ObjectCreatedEvent(ob))
            name = INameChooser(self.context).chooseName(u"", ob)
            self.context[name] = ob

            self.request.response.setStatus(202)
            return None

        return self.index()
