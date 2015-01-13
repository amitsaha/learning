CC = gcc
PACKAGES = libsoup-2.4 gio-2.0
CFLAGS += -Wall -Werror -std=c99 $(shell pkg-config --cflags $(PACKAGES))
LIBS = $(shell pkg-config --libs $(PACKAGES))

simple_server: 	simple_server.o
	$(CC) -o $@ $^ $(LIBS)

simple_server.o:	simple_server.c

clean:
	rm simple_server.o simple_server
