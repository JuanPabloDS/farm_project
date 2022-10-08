from django.contrib.gis.db import models
from django.utils.translation import gettext as _
from farm_base.models import Owner


class Farm(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255,
                            null=True, blank=False)

    geometry = models.GeometryField(verbose_name=_("Geometry"),
                                    null=True, blank=True)

    area = models.FloatField(verbose_name=_("Area"),
                             blank=True, null=True)

    municipality = models.CharField(verbose_name= ('Municipality'), max_length=255,
                            null=True, blank=False)
    
    state = models.CharField(verbose_name= ('State'), max_length=150,
                            null=True, blank=False)
    
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    centroid = models.PointField(verbose_name=_("Centroid"),
                                 blank=True, null=True)

    creation_date = models.DateTimeField(verbose_name=_("Creation date"),
                                         auto_now_add=True, editable=False)

    last_modification_date = models.DateTimeField(
        verbose_name=_("Last modification date"), auto_now=True)

    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['id']
        verbose_name = _('Farm')
        verbose_name_plural = _('Farms')
