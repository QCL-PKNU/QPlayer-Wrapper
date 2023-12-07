# 컴파일러
CXX = g++

# 외부 프로젝트 소스 파일
SOURCE = core.cpp

# 내부 프로젝트 헤더 파일과 라이브러리 경로
INNER_INCLUDE = -IQPlayer/qasm
INNER_LIBRARY = -LQPlayer/release/lib -libqplayer.a

# 빌드 명령어
all: outerProject

outerProject: $(SOURCE)
    $(CXX) -o $@ $^ $(INNER_INCLUDE) $(INNER_LIBRARY)
	pip install -e .

clean:
    rm -f outerProject

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