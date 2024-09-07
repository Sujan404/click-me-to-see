from django_seeding import seeders
from django_seeding.seeder_registry import SeederRegistry
from blog import models
@SeederRegistry.register
class CategorySeeder(seeders.JSONFileModelSeeder):
    model = models.Category
    json_file_path = 'seeder_data/category.json'