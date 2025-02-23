.PHONY: init test

init:
	pip install -r requirements.txt

test:
	python -m unittest discover -s tests -p "*_test.py"

automatic-test:
	while inotifywait -e close_write -r src tests; do make test; done
