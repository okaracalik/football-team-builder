import unittest
import requests
import json

BASE_URL = "http://localhost:8051"

FORMATION_5_3_2 = [
    'gk',
    'rcb', 'cb', 'lcb',
    'rwb', 'lwb',
    'rcm', 'lcm',
    'cam',
    'rs', 'ls',
]

FORMATION = FORMATION_5_3_2
BUDGET = 200 * 10**6

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

  def test_players_get_endpoint_sublevel_2(self):
    response = requests.get(f"{BASE_URL}/players/some")
    assert response.status_code == 403
    assert response.headers["Content-Type"] == 'application/json'

  def test_players_post_endpoint(self):
    response = requests.post(f"{BASE_URL}/players")
    assert response.status_code == 403

  def test_players_post_team_endpoint(self):
    data = json.dumps({'formation': FORMATION, 'budget': BUDGET})
    response = requests.post(f"{BASE_URL}/players/team", data=data)
    assert response.status_code == 200

  def test_players_post_team_invalid_endpoint(self):
    data = json.dumps({'key': 'value', 'arr': ['a', 'b']})
    response = requests.post(f"{BASE_URL}/players/team", data=data)
    assert response.status_code == 400

  def test_players_post_other_endpoint(self):
    response = requests.post(f"{BASE_URL}/players/any")
    assert response.status_code == 403

  def test_players_put_endpoint(self):
    response = requests.put(f"{BASE_URL}/players")
    assert response.status_code == 405

  def test_players_delete_endpoint(self):
    response = requests.delete(f"{BASE_URL}/players")
    assert response.status_code == 405

  def test_assets_endpoint(self):
    response = requests.delete(f"{BASE_URL}/assets/players/000016.png")
    assert response.status_code == 200

  def test_invalid_endpont(self):
    response = requests.delete(f"{BASE_URL}/random")
    assert response.status_code == 403


if __name__ == "__main__":
    unittest.main()