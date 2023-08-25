from django.contrib import admin


class ProducerConsumerAdminSite(admin.AdminSite):
    title_header = 'Producer-Consumer Admin'
    site_header = 'Producer-Consumer administration'
    index_title = 'Producer-Consumer site admin'
