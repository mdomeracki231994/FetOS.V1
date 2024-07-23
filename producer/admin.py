from django.contrib import admin

from producer.models import Producer, ProducerStore

admin.site.register(Producer)
admin.site.register(ProducerStore)
