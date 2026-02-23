from API_Yougile import API
from Initial_data import BASE_URL, HEADERS, USER_ID, get_unique_title


# ==================== ПОЗИТИВНЫЕ ТЕСТЫ ====================

def test_create_project():
    api = API(BASE_URL, HEADERS)
    title = get_unique_title()

    resp = api.create_project(title, USER_ID)
    assert resp.status_code in [200, 201]

    project_id = resp.json().get("id")
    assert project_id is not None

    delete_resp = api.delete_project(project_id)
    assert delete_resp.status_code in [200, 204, 404]


def test_update_project_title():
    api = API(BASE_URL, HEADERS)
    title = get_unique_title()

    resp = api.create_project(title, USER_ID)
    assert resp.status_code in [200, 201]
    project_id = resp.json().get("id")
    assert project_id is not None

    new_title = get_unique_title()
    update_resp = api.update_project(project_id, {"title": new_title})
    assert update_resp.status_code in [200, 204]

    get_resp = api.get_project(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json().get("title") == new_title

    delete_resp = api.delete_project(project_id)
    assert delete_resp.status_code in [200, 204, 404]


def test_get_project_by_id():
    api = API(BASE_URL, HEADERS)
    title = get_unique_title()

    resp = api.create_project(title, USER_ID)
    assert resp.status_code in [200, 201]
    project_id = resp.json().get("id")
    assert project_id is not None

    get_resp = api.get_project(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json().get("id") == project_id

    delete_resp = api.delete_project(project_id)
    assert delete_resp.status_code in [200, 204, 404]


# ==================== НЕГАТИВНЫЕ ТЕСТЫ ====================

def test_create_project_empty_title():
    api = API(BASE_URL, HEADERS)
    empty_title = ""

    resp = api.create_project(empty_title, USER_ID)
    assert resp.status_code not in [200, 201]


def test_get_project_nonexistent_id():
    api = API(BASE_URL, HEADERS)
    fake_id = "00000000-0000-0000-0000-000000000000"

    resp = api.get_project(fake_id)
    assert resp.status_code not in [200, 201]


def test_update_project_nonexistent_id():
    api = API(BASE_URL, HEADERS)
    fake_id = "00000000-0000-0000-0000-000000000000"

    resp = api.update_project(fake_id, {"title": "Test"})
    assert resp.status_code not in [200, 201]
