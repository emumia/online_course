# Generated by Django 4.2.2 on 2023-06-15 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        choices=[
                            (
                                "Python with Problem Solving",
                                "Python with Problem Solving",
                            ),
                            (
                                "Data Science & Machine Learning",
                                "Data Science & Machine Learning",
                            ),
                            ("Become a Data Analyst", "Become a Data Analyst"),
                            (
                                "Deep Learning for NLP & CV",
                                "Deep Learning for NLP & CV",
                            ),
                            (
                                "Become a Big Data Engineer",
                                "Become a Big Data Engineer",
                            ),
                            ("Cloud Computing with AWS", "Cloud Computing with AWS"),
                            ("Django for Web & AI", "Django for Web & AI"),
                            (
                                "Statistics for Data Science",
                                "Statistics for Data Science",
                            ),
                        ],
                        max_length=100,
                    ),
                ),
                ("type_of_course", models.CharField(max_length=50)),
                ("fee_of_course", models.IntegerField()),
                ("batch", models.IntegerField()),
                ("discount_course", models.IntegerField()),
                ("start_date_course", models.CharField(max_length=50)),
                ("course_video_link", models.CharField(max_length=1000)),
                ("first_description", models.CharField(max_length=2000)),
                ("second_description", models.CharField(max_length=2000)),
                ("duration_of_course", models.IntegerField(max_length=20)),
                ("class_time", models.CharField(max_length=50)),
                ("teacher_name", models.CharField(max_length=200)),
                ("teacher_image", models.ImageField(upload_to="teacher_img")),
                ("image1_course", models.ImageField(upload_to="course1_img")),
                ("image2_course", models.ImageField(upload_to="course2_img")),
                ("post_date", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
