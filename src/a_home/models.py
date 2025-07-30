from django.db import models
from django.utils.translation import gettext_lazy as _


class HomePageContent(models.Model):
    """Model to store the content for the home page."""

    title = models.CharField(_("Title"), max_length=200)
    content = models.TextField(_("Content"), help_text=_("Content in Markdown format."))
    is_active = models.BooleanField(
        _("Is Active"),
        default=False,
        help_text=_(
            "Designates this as the active content for the home page. Only one entry should be active."
        ),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Home Page Content")
        verbose_name_plural = _("Home Page Content")
