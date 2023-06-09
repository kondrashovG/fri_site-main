# from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

# User = get_user_model()

# Create your models here.
class Account(models.Model):
    account = models.CharField(_('Cчёт'), max_length=55, unique=True)

    class Meta:
        verbose_name = _('счёт')
        verbose_name_plural = _('счета')

class Operation(models.Model):
    purpose_of_payment = models.CharField(_('назначение платежа'), max_length=255, unique=True)
    summ = models.DecimalField(_('сумма'), max_digits=11, decimal_places=2)
    from_account = models.ForeignKey(Account, related_name='f_acc', on_delete=models.PROTECT,
                                     verbose_name=_('счёт списания'))
    to_account = models.ForeignKey(Account, related_name='t_acc', on_delete=models.PROTECT,
                                   verbose_name=_('счёт зачисления'))
    time_operation = models.DateTimeField(_('время проводки'), auto_now_add=True)

    class Meta:
        ordering = ('-time_operation',)
        verbose_name = _('транзакция')
        verbose_name_plural = _('транзакции')

class Fund(models.Model):
    name = models.CharField(_('наименование фонда'), max_length=255, unique=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('фонд')
        verbose_name_plural = _('фонды')

