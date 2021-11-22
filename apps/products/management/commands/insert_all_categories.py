from django.core.management.base import BaseCommand, CommandError
import os, json
from apps.products.models import *

module_dir = os.path.dirname(__file__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(os.path.join(module_dir, 'main_categories.json'), 'r') as main_category:
            data = json.loads(main_category.read())
        for c_name in data['data']:
            category_ins = Category.get_or_create(value=c_name['name'])

        with open(os.path.join(module_dir, 'sub_categories.json'), 'r') as sub_category:
            data = json.loads(sub_category.read())
            for sub_name in data['data']:
                category_ins = SubCategory.get_or_create(value=sub_name['name'])

        with open(os.path.join(module_dir, 'sup_categories.json'), 'r') as sup_category:
            data = json.loads(sup_category.read())
            for sup_name in data['data']:
                category_ins = SupCategory.get_or_create(value=sup_name['name'])

        with open(os.path.join(module_dir, 'add_categories.json'), 'r') as add_category:
            data = json.loads(add_category.read())
            for add_name in data['data']:
                category_ins = AddCategory.get_or_create(value=add_name['name'])
