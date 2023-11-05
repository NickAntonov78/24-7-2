from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os

pf = PetFriends()


def test_get_api_key_for_invalid_user(email=invalid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403

def test_get_api_key_for_invalid_user_pass(email=valid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403

def test_get_api_key_for_invalid_user_and_pass(email=invalid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403

def test_add_new_pet_with_invalid_data(name='Барбоскин', animal_type='двортерьер', age='0.2', pet_photo='images/pet-76.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 403   #Баг возраст питомца меньше года, а сайт принимает его.

def test_successful_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/vid.mp4")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 403 #Баг при 0 питомцев создается питомец с видео вместо фото

def test_add_new_pet_with_invalid_data(name='Барбоскин', animal_type='двортерьер', age='4', pet_photo='images/vid.mp4'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 403  #Баг питомец добавляется с видео вместо фото

def test_add_new_pet_with_invalid_data(name='Барбоскин', animal_type='двортерьер', age='4', pet_photo='images/122.gif'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 403  #Баг питомец добавляется с фото формата не JPG, JPEG или PNG

def test_add_new_pet_with_invalid_data(name='', animal_type='', age='', pet_photo='images/pet-76.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 403 #Баг питомца можно создать с пустыми графами имени, типа и возраста

def test_add_new_pet_with_invalid_data(name='Барбоскин', animal_type='двортерьер', age='два', pet_photo='images/pet-76.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 403 #Баг сайт принимает строку вместо числа в графе возраст

def test_add_new_pet_with_invalid_data(name='Барбоскин', animal_type='двортерьер', age='0.2', pet_photo='images/pet-76.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 403

def test_add_new_pet_with_invalid_data(name='Яэь', animal_type='двортерьер', age='2', pet_photo='images/121231313.txt'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 403 #Баг сайт принимает текстовый документ вместо фото

