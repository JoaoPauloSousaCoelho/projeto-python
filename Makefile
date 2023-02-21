install:
		@poetry install
		
format:
		@isort . --check
		@blue . --check
		

test:
		@pytest -v

sec:
		@pip-audit		



