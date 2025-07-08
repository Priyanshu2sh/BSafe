# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApprovedWorkPermit(models.Model):
    permit_to_work = models.ForeignKey('PermitToWork', models.DO_NOTHING)
    work_permit_working_at_heights = models.ForeignKey('WorkPermit', models.DO_NOTHING)
    permit_number = models.CharField(max_length=100)
    date_of_issue = models.DateField()
    time_of_issue = models.TimeField()
    permit_expiration_date = models.DateField()
    helmet = models.IntegerField(blank=True, null=True)
    safety_harness = models.IntegerField(blank=True, null=True)
    high_visibility_vest = models.IntegerField(blank=True, null=True)
    non_slip_footwear = models.IntegerField(blank=True, null=True)
    gloves = models.IntegerField(blank=True, null=True)
    other_specify = models.TextField(blank=True, null=True)
    rescue_plan_in_place = models.IntegerField(blank=True, null=True)
    emergency_contact_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'approved_work_permit'


class Assign(models.Model):
    department_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    target_start_date = models.DateField()
    target_end_date = models.DateField()
    category_id = models.PositiveIntegerField()
    issue = models.TextField()
    is_assigned = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assign'


class CampaignAudioMessages(models.Model):
    campaign_id = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    audio_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_audio_messages'


class Categories(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Departments(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(unique=True, max_length=20, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    head = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class EmergencyAlertTypes(models.Model):
    type = models.CharField(max_length=255)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergency_alert_types'


class EmergencyAlerts(models.Model):
    emergency_alert_type = models.CharField(max_length=50)
    alert_from = models.ForeignKey('UsersBackup', models.DO_NOTHING, db_column='alert_from', blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    voice = models.CharField(max_length=255, blank=True, null=True)
    other_type = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergency_alerts'


class Groups(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'groups'


class Hsnmanagercontact(models.Model):
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hsnmanagercontact'


class IncidentReporting(models.Model):
    incident_reporting_type = models.CharField(max_length=100)
    report_from = models.ForeignKey('UsersBackup', models.DO_NOTHING, db_column='report_from', blank=True, null=True)
    incident = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    voice = models.CharField(max_length=255, blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incident_reporting'


class IncidentReportingTypes(models.Model):
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'incident_reporting_types'


class LoginAttempts(models.Model):
    ip_address = models.CharField(max_length=16)
    login = models.CharField(max_length=100, blank=True, null=True)
    time = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_attempts'


class Otp(models.Model):
    mobile = models.CharField(max_length=20)
    otp = models.CharField(max_length=10)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'otp'


class PermitToWork(models.Model):
    user_id = models.IntegerField()
    work_permit_id = models.IntegerField()
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    status = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    approve_by_supervisor = models.IntegerField(blank=True, null=True)
    approve_by_safety_officer = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permit_to_work'


class PermitToWorkTypes(models.Model):
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'permit_to_work_types'


class PpeGallery(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ppe_gallery'


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    sku = models.CharField(unique=True, max_length=100, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Projects(models.Model):
    project_name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'


class SosCalls(models.Model):
    sos_name = models.CharField(max_length=100)
    user_id = models.IntegerField()
    number = models.CharField(max_length=20)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sos_calls'


class Stations(models.Model):
    station_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stations'


class Tasks(models.Model):
    task_name = models.CharField(max_length=255)
    priority = models.CharField(max_length=6)
    task_type = models.CharField(max_length=100)
    target_date = models.DateField(blank=True, null=True)
    frequency = models.CharField(max_length=100, blank=True, null=True)
    task_description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=60, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks'


class Users(models.Model):
    ip_address = models.CharField(max_length=45)
    username = models.CharField(max_length=100, blank=True, null=True)
    employee_id = models.CharField(max_length=122, blank=True, null=True)
    qualification = models.CharField(max_length=122, blank=True, null=True)
    course_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=254)
    activation_selector = models.CharField(unique=True, max_length=255, blank=True, null=True)
    activation_code = models.CharField(max_length=255, blank=True, null=True)
    forgotten_password_selector = models.CharField(unique=True, max_length=255, blank=True, null=True)
    forgotten_password_code = models.CharField(max_length=255, blank=True, null=True)
    forgotten_password_time = models.PositiveIntegerField(blank=True, null=True)
    remember_selector = models.CharField(unique=True, max_length=255, blank=True, null=True)
    remember_code = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.PositiveIntegerField()
    last_login = models.PositiveIntegerField(blank=True, null=True)
    active = models.PositiveIntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    reporting_manager_id = models.IntegerField(blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    designation = models.CharField(max_length=150, blank=True, null=True)
    current_location = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=40, blank=True, null=True)
    photo = models.CharField(max_length=250, blank=True, null=True)
    isupdate = models.IntegerField(blank=True, null=True)
    track_id = models.CharField(max_length=23, blank=True, null=True)
    issue = models.CharField(max_length=50, blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersBackup(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    current_location = models.CharField(max_length=255, blank=True, null=True)
    reporting_manager = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_backup'


class UsersGroups(models.Model):
    user_id = models.PositiveIntegerField()
    group_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'users_groups'


class WorkPermit(models.Model):
    permit_to_work_type_id = models.IntegerField()
    ppe_id = models.CharField(max_length=224, blank=True, null=True)
    ptw_request_initiated = models.CharField(max_length=255, blank=True, null=True)
    entity_name = models.CharField(max_length=255, blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    worksite_location = models.CharField(max_length=255, blank=True, null=True)
    description_of_work = models.TextField(blank=True, null=True)
    work_location_height_level = models.CharField(max_length=255, blank=True, null=True)
    duration_from = models.DateTimeField(blank=True, null=True)
    duration_to = models.DateTimeField(blank=True, null=True)
    risk_of_falling = models.IntegerField(blank=True, null=True)
    safety_harness = models.IntegerField(blank=True, null=True)
    guardrails = models.IntegerField(blank=True, null=True)
    ladders_scaffolds = models.IntegerField(blank=True, null=True)
    safety_nets = models.IntegerField(blank=True, null=True)
    other_specify = models.IntegerField(blank=True, null=True)
    weather_condition_affect_safety = models.IntegerField(blank=True, null=True)
    name_of_workers = models.TextField(blank=True, null=True)
    first_aid_trained_personnel_on_site = models.CharField(max_length=255, blank=True, null=True)
    rescue_plan_in_place = models.IntegerField(blank=True, null=True)
    rescue_plan_file = models.CharField(max_length=255, blank=True, null=True)
    contact_person_name = models.CharField(max_length=255, blank=True, null=True)
    contact_person_number = models.CharField(max_length=20, blank=True, null=True)
    approve_by_supervisor = models.IntegerField(blank=True, null=True)
    approve_by_safety_officer = models.IntegerField(blank=True, null=True)
    overall_status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_permit'
