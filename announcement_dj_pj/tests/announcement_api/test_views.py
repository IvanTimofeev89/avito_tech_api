
import pytest
from django.urls import reverse
from rest_framework import status
from announcement_api.models import Ad

@pytest.mark.django_db
def test_create_ad(api_client, test_image):

    url = reverse('ad-list')
    data = {
        "name": "New Ad",
        "description": "New Description",
        "price": 150,
        "uploaded_pictures": [test_image],
    }
    response = api_client.post(url, data, format='multipart')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['status'] == 'success'
    assert Ad.objects.count() == 1

@pytest.mark.django_db
def test_list_ads(api_client, create_ads):
    url = reverse('ad-list')
    response = api_client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 3

@pytest.mark.django_db
def test_list_ads_with_fields(api_client, create_ads):
    url = reverse('ad-list') + '?fields=true'
    response = api_client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 3
    assert 'name' in response.data['results'][0]

@pytest.mark.django_db
def test_ordering_ads(api_client, create_ads):
    url = reverse('ad-list') + '?ordering=-price'
    response = api_client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]['price'] == 300

@pytest.mark.django_db
def test_create_ad_invalid_data(api_client):
    url = reverse('ad-list')
    data = {
        "name": "",
        "description": "No Title",
        "price": 150
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['status'] == 'failure'
