init:
	pip install -r requirements.txt
	@echo '----------------init-------------------'

test:
	nosetests tests

clone_repo:
	#  check if there is QPlayer folder if not clone it
	if [ ! -d "QPlayer" ]; then \
		git clone https://github.com/eQuantumOS/QPlayer.git; \
	fi