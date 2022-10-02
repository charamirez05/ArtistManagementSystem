# Generated by Django 4.1.1 on 2022-09-30 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('ArtistID', models.AutoField(primary_key=True, serialize=False)),
                ('ArtistName', models.CharField(max_length=30)),
                ('DebutDate', models.DateField()),
                ('YearsActive', models.IntegerField(default=1)),
                ('isActor', models.BooleanField(default=False)),
                ('isSinger', models.BooleanField(default=False)),
                ('Birthdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Singles',
            fields=[
                ('SingleID', models.AutoField(primary_key=True, serialize=False)),
                ('SingleName', models.CharField(max_length=30)),
                ('RecordedDate', models.DateField()),
                ('ReleasedDate', models.DateField()),
                ('Genre', models.CharField(max_length=20)),
                ('Composer', models.CharField(max_length=30)),
                ('Producer', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('artist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='registration.artist')),
                ('nationality', models.CharField(max_length=30)),
            ],
            bases=('registration.artist',),
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('artist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='registration.artist')),
                ('Genre', models.CharField(max_length=50)),
                ('FandomName', models.CharField(max_length=50)),
                ('IsSolo', models.BooleanField(default=False)),
                ('IsGroup', models.BooleanField(default=False)),
            ],
            bases=('registration.artist',),
        ),
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('albumID', models.AutoField(primary_key=True, serialize=False)),
                ('albumName', models.CharField(max_length=30)),
                ('releaseDate', models.DateField()),
                ('genre', models.CharField(max_length=30)),
                ('dateRecorded', models.DateField()),
                ('singles', models.ManyToManyField(to='registration.singles')),
                ('Singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.singer')),
            ],
        ),
        migrations.CreateModel(
            name='GroupArtist',
            fields=[
                ('singer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='registration.singer')),
                ('dateFormed', models.DateField()),
            ],
            bases=('registration.singer',),
        ),
        migrations.CreateModel(
            name='SoloArtist',
            fields=[
                ('singer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='registration.singer')),
                ('StageName', models.CharField(max_length=30)),
            ],
            bases=('registration.singer',),
        ),
        migrations.CreateModel(
            name='Songs_Included',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songsIncluded', models.CharField(max_length=50)),
                ('albums', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.albums')),
            ],
            options={
                'unique_together': {('albums', 'songsIncluded')},
            },
        ),
        migrations.AddField(
            model_name='singles',
            name='Singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.singer'),
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('platformName', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('yearEstablished', models.BigIntegerField()),
                ('ranking', models.IntegerField()),
                ('singer', models.ManyToManyField(to='registration.singer')),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=50)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.actor')),
            ],
            options={
                'unique_together': {('actor', 'specialization')},
            },
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('films', models.CharField(max_length=50)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.actor')),
            ],
            options={
                'unique_together': {('actor', 'films')},
            },
        ),
        migrations.CreateModel(
            name='Instruments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruments', models.CharField(max_length=30)),
                ('soloArtist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.soloartist')),
            ],
            options={
                'unique_together': {('soloArtist', 'instruments')},
            },
        ),
        migrations.CreateModel(
            name='GroupMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GroupMembers', models.CharField(max_length=100)),
                ('GroupArtist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.groupartist')),
            ],
            options={
                'unique_together': {('GroupArtist', 'GroupMembers')},
            },
        ),
    ]