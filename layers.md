# Карта слоёв (урок 4)

| Слой          | Преподаватель создаёт тест                            | Ученик сдаёт тест                                  |
|---------------|-------------------------------------------------------|----------------------------------------------------|
| Router        | POST /api/tests · только teacher                      | POST /api/tests/{id}/attempts · только student     |
| Schema        | TestCreate (название 3–200, тема) → TestForTeacher    | AttemptCreate (ответы) → AttemptRead (баллы)       |
| Service       | владелец — этот преподаватель; новый тест не опубликован | тест опубликован; ответов столько же, сколько вопросов |
| Repository    | TestRepository.create                                 | TestRepository.add_attempt                         |
| Model         | tests                                                 | attempts                                           |
| Ошибка → HTTP | название из 2 символов → 422                          | тест не найден → 404                               |

## Наши правила
- В Router нет SQL, в service нет HTTPException
- Секреты (пароли, токены) только в .env
