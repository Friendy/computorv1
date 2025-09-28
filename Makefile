IMAGE_NAME = computorv

CURRENT_DIR = $(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

all: build run

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -it --name $(IMAGE_NAME)_cont $(IMAGE_NAME)

run_dev:
	docker run -v $(CURRENT_DIR)/app:/usr/src -it $(IMAGE_NAME)

clean:
	docker rm -f $(IMAGE_NAME)_cont
	
fclean: clean
	docker image rm $(IMAGE_NAME)

.PHONY: build run run_dev