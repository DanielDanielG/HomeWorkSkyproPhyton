from sqlalchemy import create_engine, text


db_connection_string = "postgresql://postgres:1234@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_db_connection():
    names = db.table_names()
    assert 'subject' in names


def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute(text("select * from subject")).fetchall()
    row1 = rows[0]
    assert row1[0] == 1
    assert row1[1] == "English"


def test_insert():
    # Создание
    sql = text(
        "INSERT INTO teacher(\"teacher_id\", \"email\", \"group_id\") "
        "VALUES (:id, :mail, :sub_id)")
    db.execute(sql,
               {"id": '657904',
                "mail": 'LIyr@example.com',
                "sub_id": 77777})

    # Проверка создания
    result = db.execute(text(
        "SELECT * FROM teacher WHERE teacher_id = :id"),
          {"id": '657904'}).fetchone()
    assert result is not None

    # Удаление
    db.execute(text(
        "DELETE FROM teacher WHERE teacher_id = :id"),
        {"id": '657904'})

    # Проверка удаления
    result = db.execute(text(
        "SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": '657904'}).fetchone()
    assert result is None


def test_update():
    # Создание
    db.execute(text(
        "INSERT INTO teacher(\"teacher_id\", \"email\", \"group_id\") "
        "VALUES (:id, :mail, :sub_id)"),
               {"id": '657904',
                "mail": 'old@example.com',
                "sub_id": 77777})

    # Проверка создания
    result = db.execute(text(
        "SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": '657904'}).fetchone()
    assert result is not None

    # Обновление
    sql = text(
        "UPDATE teacher SET email = :mail WHERE "
        "teacher_id = :id")
    db.execute(sql, {
        "mail": 'New descr',
        "id": '657904'})

    # Проверка обновления
    result = db.execute(text(
        "SELECT email FROM teacher WHERE teacher_id = :id"),
        {"id": '657904'}).fetchone()
    assert result[0] == 'New descr'

    # Удаление
    db.execute(text(
        "DELETE FROM teacher WHERE teacher_id = :id"),
        {"id": '657904'})

    # Проверка удаления
    result = db.execute(text(
        "SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": '657904'}).fetchone()
    assert result is None


def test_delete():
    # Создание записи
    db.execute(text(
        "INSERT INTO teacher(\"teacher_id\", \"email\", \"group_id\") "
        "VALUES (:id, :mail, :sub_id)"),
               {"id": '657904',
                "mail": 'todelete@example.com',
                "sub_id": 77777})

    # Проверка создания
    result = db.execute(text(
        "SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": '657904'}).fetchone()
    assert result is not None

    # Удаление
    sql = text("DELETE FROM teacher WHERE teacher_id = :id")
    db.execute(sql, {"id": '657904'})

    # Проверка удаления
    result = db.execute(text(
        "SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": '657904'}).fetchone()
    assert result is None


def test_insert_multiple():
    # Создание нескольких записей
    sql = text(
        "INSERT INTO teacher(\"teacher_id\", \"email\", \"group_id\") "
        "VALUES (:id, :mail, :sub_id)")
    db.execute(sql,
               {"id": 900001,
                "mail": 'multi1@example.com',
                "sub_id": 100})
    db.execute(sql,
               {"id": 900002,
                "mail": 'multi2@example.com',
                "sub_id": 200})
    db.execute(sql,
               {"id": 900003,
                "mail": 'multi3@example.com',
                "sub_id": 300})

    # Проверка создания
    result1 = db.execute(text(
        "SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": 900001}).fetchone()
    result2 = db.execute(text(
        "SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": 900002}).fetchone()
    result3 = db.execute(text(
        "SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": 900003}).fetchone()
    assert result1 is not None
    assert result2 is not None
    assert result3 is not None

    # Удаление
    db.execute(text(
        "DELETE FROM teacher WHERE teacher_id = :id"),
        {"id": 900001})
    db.execute(text(
        "DELETE FROM teacher WHERE teacher_id = :id"),
        {"id": 900002})
    db.execute(text(
        "DELETE FROM teacher WHERE teacher_id = :id"),
        {"id": 900003})

    # Проверка удаления
    result1 = db.execute(text(
        "SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": 900001}).fetchone()
    result2 = db.execute(text(
        "SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": 900002}).fetchone()
    result3 = db.execute(text(
        "SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": 900003}).fetchone()
    assert result1 is None
    assert result2 is None
    assert result3 is None


def test_select_with_filter():
    # Создание записи
    db.execute(text(
        "INSERT INTO teacher(\"teacher_id\", \"email\", \"group_id\") "
        "VALUES (:id, :mail, :sub_id)"),
        {"id": 900010,
         "mail": 'filter_test@example.com',
         "sub_id": 555})

    # Проверка создания
    result = db.execute(text(
        "SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": 900010}).fetchone()
    assert result is not None

    # Выборка с WHERE по email
    result = db.execute(text(
        "SELECT * FROM teacher WHERE email = :mail"),
        {"mail": 'filter_test@example.com'}).fetchone()
    assert result is not None
    assert result[1] == 'filter_test@example.com'

    # Выборка с WHERE по group_id
    result = db.execute(text(
        "SELECT * FROM teacher WHERE group_id = :gid"),
        {"gid": 555}).fetchone()
    assert result is not None
    assert result[2] == 555

    # Удаление
    db.execute(text(
        "DELETE FROM teacher WHERE teacher_id = :id"),
        {"id": 900010})

    # Проверка удаления
    result = db.execute(text(
        "SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": 900010}).fetchone()
    assert result is None
