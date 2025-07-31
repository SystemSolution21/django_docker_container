from django.db import models
from django.utils.translation import gettext_lazy as _


class HomePageContent(models.Model):
    """Model to store the content for the home page."""

    title = models.CharField(_("Title"), max_length=200)
    content = models.TextField(
        _("Content"),
        help_text=_(
            "Content can be written in Markdown or HTML. To parse Markdown inside an HTML block, add the attribute "
            '`markdown="1"` to the tag. Example: &lt;div markdown="1"&gt;# A Header&lt;/div&gt;. '
            'Note: Use the "Source Code" view in the editor when adding blocks with `markdown="1"`.'
        ),
    )
    is_active = models.BooleanField(
        _("Is Active"),
        default=False,
        help_text=_(
            "Designates this as the active content for the home page. Only one entry should be active."
        ),
    )

    def save(self, *args, **kwargs):
        # If this instance is being marked as active, ensure no other instances are.
        if self.is_active:
            # Select all other active instances and update them to be inactive.
            # .exclude(pk=self.pk) is important to ensure we don't deactivate
            # the current instance if it's being updated.
            HomePageContent.objects.filter(is_active=True).exclude(pk=self.pk).update(
                is_active=False
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Home Page Content")
        verbose_name_plural = _("Home Page Content")
