from django.contrib.admin.apps import AdminConfig


class TableAdminConfig(AdminConfig):
    default_site = 'admin.ProducerConsumerAdminSite'
