# Generated by Django 5.2 on 2025-05-04 20:39

from django.db import migrations, models
from django.utils.text import slugify

def slugify_artwork_title(apps, schema_editor):
    Artwork = apps.get_model('artworks', 'Artwork')
    for artwork in Artwork.objects.all():
        artwork.slug = slugify(artwork.category.name + "-" + artwork.title + "-" + artwork.created_at.strftime("%Y%m%d%H%M%S"))
        print(artwork.slug)
        artwork.save()


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.RunPython(slugify_artwork_title),
    ]

