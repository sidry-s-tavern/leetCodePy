# Структура данных об организациях.
organizations = {
    1: {
        'name': 'Организация',
        'reviews': []
    },
    2: {
        'name': 'Другая организация',
        'reviews': []
    },
}

# Необходимо напиcать функцию, которая добавляет отзыв об организации в структуру данных (выше).
# Функция должна возвращать добавленный отзыв.
# У организации может быть только один отзыв от каждого пользователя.

# валидация пользователя - на стороне разраба
# количество организаций - 2 что есть

def add_review(user: str, comment: str, nameOfOrg: str) -> dict:

    org_id = None
    for org_key, org_data in organizations.items():
        if org_data['name'] == nameOfOrg:
            org_id = org_key

    if org_id is None:
        raise ValueError(f"Организация '{nameOfOrg}' не найдена")

    review_model = {
        'user': user,
        'comment': comment
    }

    org_reviews = organizations[org_id]['reviews']
    for review in org_reviews:
        if review['user'] == user:
            raise ValueError(f"Пользователь '{user}' уже оставил отзыв для организации '{nameOfOrg}'")

    organizations[org_id]['reviews'].append(review_model)

    return review_model
