CC = gcc
PACKAGES = libsoup-2.4
CFLAGS += -Wall -Werror -std=c99 $(shell pkg-config --cflags $(PACKAGES))
LIBS = $(shell pkg-config --libs $(PACKAGES))

simple_get: 	simple_get.o
	$(CC) -o $@ $^ $(LIBS)

simple_get.o:	simple_get.c

clean:
	rm simple_get.o simple_get
