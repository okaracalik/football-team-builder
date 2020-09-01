import unittest
import requests

BASE_URL = "http://localhost:8051"

class ApiTests(unittest.TestCase):

  def test_server_works(self):
    response = requests.get(BASE_URL)
    assert response.status_code == 200

  def test_players_head_endpoint(self):
    response = requests.head(f"{BASE_URL}/players")
    assert response.status_code == 200

  def test_players_get_endpoint(self):
    response = requests.get(f"{BASE_URL}/players")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == 'application/json'

  def test_players_get_endpoint_sublevel_1(self):
    response = requests.get(f"{BASE_URL}/players/some")
    assert response.status_code == 501
    assert response.headers["Content-Type"] == 'application/json'

  def test_players_get_endpoint_sublevel_2(self):
    response = requests.get(f"{BASE_URL}/players/some/some")
    assert response.status_code == 403
    assert response.headers["Content-Type"] == 'application/json'

  def test_players_post_endpoint(self):
    response = requests.post(f"{BASE_URL}/players")
    assert response.status_code == 405

  def test_players_put_endpoint(self):
    response = requests.put(f"{BASE_URL}/players")
    assert response.status_code == 405

  def test_players_delete_endpoint(self):
    response = requests.delete(f"{BASE_URL}/players")
    assert response.status_code == 405

  def test_invalid_endpont(self):
    response = requests.delete(f"{BASE_URL}/random")
    assert response.status_code == 403


if __name__ == "__main__":
    unittest.main()