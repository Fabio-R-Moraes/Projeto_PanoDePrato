# from inspect import signature
from random import randint
from faker import Faker

def rand_ratio():
     return randint(840, 900), randint(473, 573)

fake = Faker('pt_BR')

 # print(signature(fake.random_number))
def make_recipe():
     return {'id': fake.random_number(digits=2, fix_len=True),'title': fake.sentence(nb_words=6),
             'description': fake.sentence(nb_words=12),'valor_preco': fake.random_number(digits=2, fix_len=True),
             'valor_preco_unit': 'Reais','created_at': fake.date_time(),
             'author': {'first_name': fake.first_name(),'last_name': fake.last_name(),},
             'category': {'name': fake.word()},'cover': {'url': 'https://loremflickr.com/%s/%s/art,church' % rand_ratio(),}}
     
if __name__ == '__main__':
     from pprint import pprintp
     print(make_recipe())