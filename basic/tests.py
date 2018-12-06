from django.test import TestCase
from .models import AVItem
# Create your tests here.
class HomePageTest(TestCase):
    '''
        Passes if home template is used at startup
    '''
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'basic/home.html')

class ItemModelsTest(TestCase):

    def test_saving_and_retrieving_items(self):
        '''
            Ensures items are properly modeled
        '''
        first_avitem_ = AVItem()
        first_avitem_.item_title = 'My First avitem'
        first_avitem_.save()

        second_avitem_ = AVItem()
        second_avitem_.item_title = 'My Second avitem'
        second_avitem_.save()

        saved_items = AVItem.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.item_title, 'My First avitem')
        self.assertEqual(second_saved_item.item_title, 'My Second avitem')
