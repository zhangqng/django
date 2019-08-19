# Generated by Django 2.2.4 on 2019-08-17 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bugname', models.CharField(max_length=64, verbose_name='bug名称')),
                ('bugdetail', models.CharField(max_length=200, verbose_name='详情')),
                ('bugstatus', models.CharField(choices=[('激活', '激活'), ('已解决', '已解决'), ('已关闭', '已关闭')], default='激活', max_length=200, null=True, verbose_name='解决状态')),
                ('buglevel', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='3', max_length=200, null=True, verbose_name='严重程度')),
                ('bugcreater', models.CharField(max_length=200, verbose_name='创建人')),
                ('bugassign', models.CharField(max_length=200, verbose_name='分配给')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'verbose_name': 'bug管理',
                'verbose_name_plural': 'bug管理',
            },
        ),
    ]
