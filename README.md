# stepik_tester_final_task

### Примерная последовательность действий для Linux. Для Windows я думаю Вы сможете приспособить
- $ git clone https://github.com/pashkovka115/stepik_tester_final_task.git
- $ cd stepik_tester_final_task
- $ python3 -m venv venv
- $ source venv/bin/activate
- $ pip install -r requirements.txt
- $ pytest -v --tb=line --language=en -m need_review

### Запуск тестов для ревью
pytest -v --tb=line --language=en -m need_review

### Запуск всех тестов
pytest -v -s --tb=line
