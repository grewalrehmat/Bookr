# Generated by Django 5.1.5 on 2025-01-26 16:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_book_publisher_alter_publisher_website_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='contributor',
            name='last_name',
        ),
        migrations.AddField(
            model_name='contributor',
            name='first_names',
            field=models.CharField(default='Unknown', help_text="The contributor's first name or names.", max_length=50),
        ),
        migrations.AddField(
            model_name='contributor',
            name='last_names',
            field=models.CharField(default='Unknown', help_text="The contributor's last name or names.", max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(verbose_name='Date the book was published.'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.publisher'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(help_text='The title of the book.', max_length=70),
        ),
        migrations.AlterField(
            model_name='bookcontributor',
            name='role',
            field=models.CharField(choices=[('AUTHOR', 'Author'), ('CO_AUTHOR', 'Co-Author'), ('EDITOR', 'Editor')], max_length=20, verbose_name='The role this contributor had in the book.'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='email',
            field=models.EmailField(help_text="The Publisher's email address.", max_length=254),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(help_text='The name of the Publisher.', max_length=50),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(help_text="The Publisher's website."),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='The Review text.')),
                ('rating', models.IntegerField(help_text='The rating the reviewer has given.')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='The date and time the review was created.')),
                ('date_edited', models.DateTimeField(help_text='The date and time the review was last edited.', null=True)),
                ('book', models.ForeignKey(help_text='The Book that this review is for.', on_delete=django.db.models.deletion.CASCADE, to='reviews.book')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
