check-style:
	flake8 --exclude="migrations" .

all: check-style
