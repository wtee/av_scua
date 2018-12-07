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
        # first test item
        first_avitem_ = AVItem()
        first_avitem_.uid = 'hello uid'
        first_avitem_.item_title='hello item_title'
        first_avitem_.original_id='hello original_id'
        first_avitem_.collection_id='hello collection_id'
        first_avitem_.series_title='hello series_title'
        first_avitem_.episode_title='hello episode_title'
        first_avitem_.can_number='hello can_number'
        first_avitem_.original_can_number='hello original_can_number'
        first_avitem_.call_number='hello call_number'
        first_avitem_.date_created='hello date_created'
        first_avitem_.credits='hello credits'
        first_avitem_.description='hello description'
        first_avitem_.location='hello location'
        first_avitem_.save()

        # second test item
        second_avitem_ = AVItem()
        second_avitem_.uid = 'goodbye uid'
        second_avitem_.item_title='goodbye item_title'
        second_avitem_.original_id='goodbye original_id'
        second_avitem_.collection_id='goodbye collection_id'
        second_avitem_.series_title='goodbye series_title'
        second_avitem_.episode_title='goodbye episode_title'
        second_avitem_.can_number='goodbye can_number'
        second_avitem_.original_can_number='goodbye original_can_number'
        second_avitem_.call_number='goodbye call_number'
        second_avitem_.date_created='goodbye date_created'
        second_avitem_.credits='goodbye credits'
        second_avitem_.description='goodbye description'
        second_avitem_.location='goodbye location'
        second_avitem_.save()

        saved_items = AVItem.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item_ = saved_items[0]
        second_saved_item_ = saved_items[1]

        self.assertEqual(first_saved_item_.uid, 'hello uid')
        self.assertEqual(first_saved_item_.item_title,'hello item_title')
        self.assertEqual(first_saved_item_.original_id,'hello original_id')
        self.assertEqual(first_saved_item_.collection_id,'hello collection_id')
        self.assertEqual(first_saved_item_.series_title,'hello series_title')
        self.assertEqual(first_saved_item_.episode_title,'hello episode_title')
        self.assertEqual(first_saved_item_.can_number,'hello can_number')
        self.assertEqual(first_saved_item_.original_can_number,'hello original_can_number')
        self.assertEqual(first_saved_item_.call_number,'hello call_number')
        self.assertEqual(first_saved_item_.date_created,'hello date_created')
        self.assertEqual(first_saved_item_.credits,'hello credits')
        self.assertEqual(first_saved_item_.description,'hello description')
        self.assertEqual(first_saved_item_.location,'hello location')

        self.assertEqual(second_saved_item_.uid, 'goodbye uid')
        self.assertEqual(second_saved_item_.item_title,'goodbye item_title')
        self.assertEqual(second_saved_item_.original_id,'goodbye original_id')
        self.assertEqual(second_saved_item_.collection_id,'goodbye collection_id')
        self.assertEqual(second_saved_item_.series_title,'goodbye series_title')
        self.assertEqual(second_saved_item_.episode_title,'goodbye episode_title')
        self.assertEqual(second_saved_item_.can_number,'goodbye can_number')
        self.assertEqual(second_saved_item_.original_can_number,'goodbye original_can_number')
        self.assertEqual(second_saved_item_.call_number,'goodbye call_number')
        self.assertEqual(second_saved_item_.date_created,'goodbye date_created')
        self.assertEqual(second_saved_item_.credits,'goodbye credits')
        self.assertEqual(second_saved_item_.description,'goodbye description')
        self.assertEqual(second_saved_item_.location,'goodbye location')
