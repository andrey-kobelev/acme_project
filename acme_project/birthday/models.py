from django.db import models

from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)

    last_name = models.CharField(
        'Фамилия',
        blank=True,
        help_text='Необязательное поле',
        max_length=20
    )

    birthday = models.DateField('Дата рождения', validators=(real_age,))

    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)

    class Meta:
        # Добавим к модели проверку на уникальность записи.
        constraints = (
            models.UniqueConstraint(
                # Перечень полей, совокупность которых должна быть уникальна.
                fields=('first_name', 'last_name', 'birthday'),
                # Имя ограничения.
                name='Unique person constraint',
            ),
        )
