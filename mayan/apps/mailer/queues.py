from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _

from mayan.apps.task_manager.classes import CeleryQueue
from mayan.apps.task_manager.workers import worker_slow

queue_mailing = CeleryQueue(label=_('Mailing'), name='mailing', worker=worker_slow)
queue_mailing.add_task_type(
    label=_('Send document'),
    dotted_path='mayan.apps.mailer.tasks.task_send_document'
)
