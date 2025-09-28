IMAGE_NAME = computorv

CURRENT_DIR = $(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

all: build run

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -v $(CURRENT_DIR)/app:/usr/src -it $(IMAGE_NAME)

clean:
	docker image rm $(IMAGE_NAME)

.PHONY: build run