from django.test import TestCase

# Create your tests here.

import json
original_list = [1,4,5,3]
list_as_string = json.dumps(original_list)
list_reversed_back_into_a_list = json.loads(list_as_string)
