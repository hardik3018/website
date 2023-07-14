# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-05-22 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0176_auto_20200330_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalinternfeedback',
            name='share_mentor_feedback_with_community_coordinator',
            field=models.BooleanField(default=False, help_text='If you say yes, community coordinators will be able to see your comments and the data you provided about your mentor. This helps coordinators ensure mentors are responsive, coach mentors if they are not responsive, and collect metrics they can use to fund more Outreachy internships.', verbose_name='(Optional) Do you want us to share feedback about your mentor with community coordinators?'),
        ),
        migrations.AddField(
            model_name='finalinternfeedback',
            name='time_comments',
            field=models.TextField(blank=True, help_text="(Optional) If you have not been working 40 hours a week, please let us know why. We want to support you, so let us know if there's anything we can do to help.", max_length=3000),
        ),
        migrations.AddField(
            model_name='finalmentorfeedback',
            name='mentors_report',
            field=models.TextField(default='', verbose_name='Please provide a paragraph describing what support you are providing as an Outreachy mentor. This will be shared with Outreachy organizers and your community coordinator.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='initialinternfeedback',
            name='share_mentor_feedback_with_community_coordinator',
            field=models.BooleanField(default=False, help_text='If you say yes, community coordinators will be able to see your comments and the data you provided about your mentor. This helps coordinators ensure mentors are responsive, coach mentors if they are not responsive, and collect metrics they can use to fund more Outreachy internships.', verbose_name='(Optional) Do you want us to share feedback about your mentor with community coordinators?'),
        ),
        migrations.AddField(
            model_name='initialinternfeedback',
            name='time_comments',
            field=models.TextField(blank=True, help_text="(Optional) If you have not been working 40 hours a week, please let us know why. We want to support you, so let us know if there's anything we can do to help.", max_length=3000),
        ),
        migrations.AddField(
            model_name='midpointinternfeedback',
            name='share_mentor_feedback_with_community_coordinator',
            field=models.BooleanField(default=False, help_text='If you say yes, community coordinators will be able to see your comments and the data you provided about your mentor. This helps coordinators ensure mentors are responsive, coach mentors if they are not responsive, and collect metrics they can use to fund more Outreachy internships.', verbose_name='(Optional) Do you want us to share feedback about your mentor with community coordinators?'),
        ),
        migrations.AddField(
            model_name='midpointinternfeedback',
            name='time_comments',
            field=models.TextField(blank=True, help_text="(Optional) If you have not been working 40 hours a week, please let us know why. We want to support you, so let us know if there's anything we can do to help.", max_length=3000),
        ),
        migrations.AddField(
            model_name='midpointmentorfeedback',
            name='mentors_report',
            field=models.TextField(default='', verbose_name='Please provide a paragraph describing what support you are providing as an Outreachy mentor. This will be shared with Outreachy organizers and your community coordinator.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='finalinternfeedback',
            name='hours_worked',
            field=models.CharField(choices=[('5H', '5 hours'), ('10H', '10 hours'), ('15H', '15 hours'), ('20H', '20 hours'), ('25H', '25 hours'), ('30H', '30 hours'), ('35H', '35 hours'), ('40H', '40 hours'), ('50H', '50 hours'), ('60H', '60 hours')], help_text='Include time you spend researching questions, communicating with your mentor and the community, reading about the project and the community, working on skills you need in order to complete your tasks, and working on the tasks themselves. Please be honest about the number of hours you are putting in.', max_length=3, verbose_name='What is the average number of hours per week you spend on your Outreachy internship?'),
        ),
        migrations.AlterField(
            model_name='finalinternfeedback',
            name='progress_report',
            field=models.TextField(verbose_name='Please provide a paragraph describing your progress on your project. This will only be shown to Outreachy organizers.'),
        ),
        migrations.AlterField(
            model_name='finalmentorfeedback',
            name='progress_report',
            field=models.TextField(verbose_name="Please provide a paragraph describing your intern's progress on their project. This will only be shown to Outreachy organizers, your community coordinator, and the Software Freedom Conservancy accounting staff."),
        ),
        migrations.AlterField(
            model_name='initialinternfeedback',
            name='hours_worked',
            field=models.CharField(choices=[('5H', '5 hours'), ('10H', '10 hours'), ('15H', '15 hours'), ('20H', '20 hours'), ('25H', '25 hours'), ('30H', '30 hours'), ('35H', '35 hours'), ('40H', '40 hours'), ('50H', '50 hours'), ('60H', '60 hours')], help_text='Include time you spend researching questions, communicating with your mentor and the community, reading about the project and the community, working on skills you need in order to complete your tasks, and working on the tasks themselves. Please be honest about the number of hours you are putting in.', max_length=3, verbose_name='What is the average number of hours per week you spend on your Outreachy internship?'),
        ),
        migrations.AlterField(
            model_name='initialinternfeedback',
            name='progress_report',
            field=models.TextField(verbose_name='Please provide a paragraph describing your progress on establishing communication with your mentor, and ramping up on your first tasks. This information will only be seen by Outreachy organizers. If you are having any difficulties or facing any barriers, please let us know, so we can help you.'),
        ),
        migrations.AlterField(
            model_name='initialmentorfeedback',
            name='mentors_report',
            field=models.TextField(default='', verbose_name='Please provide a paragraph describing what support you are providing as an Outreachy mentor. This will be shared with Outreachy organizers and your community coordinator.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='initialmentorfeedback',
            name='progress_report',
            field=models.TextField(verbose_name="Please provide a paragraph describing your intern's progress on establishing communication with you, connecting to your FOSS community, and ramping up on their first tasks. This will only be shown to Outreachy organizers, your community coordinators, and the Software Freedom Conservancy accounting staff."),
        ),
        migrations.AlterField(
            model_name='midpointinternfeedback',
            name='hours_worked',
            field=models.CharField(choices=[('5H', '5 hours'), ('10H', '10 hours'), ('15H', '15 hours'), ('20H', '20 hours'), ('25H', '25 hours'), ('30H', '30 hours'), ('35H', '35 hours'), ('40H', '40 hours'), ('50H', '50 hours'), ('60H', '60 hours')], help_text='Include time you spend researching questions, communicating with your mentor and the community, reading about the project and the community, working on skills you need in order to complete your tasks, and working on the tasks themselves. Please be honest about the number of hours you are putting in.', max_length=3, verbose_name='What is the average number of hours per week you spend on your Outreachy internship?'),
        ),
        migrations.AlterField(
            model_name='midpointinternfeedback',
            name='progress_report',
            field=models.TextField(verbose_name='Please provide a paragraph describing your progress on your project. This will only be shown to Outreachy organizers.'),
        ),
        migrations.AlterField(
            model_name='midpointmentorfeedback',
            name='progress_report',
            field=models.TextField(verbose_name="Please provide a paragraph describing your intern's progress on their project. This will only be shown to Outreachy organizers, your community coordinator, and the Software Freedom Conservancy accounting staff."),
        ),
    ]
