# Generated by Django 1.11.23 on 2019-09-04 18:12


from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    def migrate_data_forward(apps, schema_editor):
        updated_pub_course_ids = []
        DiscoveryCourse = apps.get_model('course_metadata', 'course')
        Course = apps.get_model('publisher', 'course')
        CourseRun = apps.get_model('publisher', 'courseRun')

        def get_publisher_course(discovery_course):
            for discovery_course_run in discovery_course.course_runs.order_by('-created'):
                if not discovery_course_run.draft:
                    publisher_course_run_counterpart = get_publisher_course_run(discovery_course_run)
                    if publisher_course_run_counterpart:
                        return publisher_course_run_counterpart.course
            return None

        def get_publisher_course_run(discovery_course_run):
            return CourseRun.objects.filter(lms_course_id = discovery_course_run.key).first()

        for discovery_course in DiscoveryCourse.everything.filter(draft=False):
            publisher_course = get_publisher_course(discovery_course)
            if publisher_course:
                publisher_course.url_slug = discovery_course.url_slug
                publisher_course.save()
                updated_pub_course_ids.append(publisher_course.id)

        for instance in Course.objects.exclude(id__in=updated_pub_course_ids):
            # clear any existing slugs to ensure uniqueness
            instance.url_slug = ''
            instance.save()

    dependencies = [
        ('publisher', '0080_remove_publisher_waffle_switches'),
        ('course_metadata', '0194_initialize_course_url_slug')
    ]

    operations = [
        migrations.RunPython(
            migrate_data_forward,
            migrations.RunPython.noop
        ),
    ]
