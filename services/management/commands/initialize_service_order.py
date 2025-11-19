from django.core.management.base import BaseCommand
from services.models import Service

class Command(BaseCommand):
    help = 'Initialize order field for existing services'

    def handle(self, *args, **options):
        services = Service.objects.filter(order=0).order_by('created_at')
        
        for index, service in enumerate(services):
            service.order = index
            service.save()
            self.stdout.write(
                self.style.SUCCESS(f'Updated service "{service.name}" with order {index}')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully initialized order for {services.count()} services')
        )