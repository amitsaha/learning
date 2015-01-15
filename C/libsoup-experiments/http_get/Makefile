CC = gcc
PACKAGES = libsoup-2.4 json-glib-1.0
CFLAGS += -Wall -Werror -std=c99 $(shell pkg-config --cflags $(PACKAGES))
LIBS = $(shell pkg-config --libs $(PACKAGES))

http_get_simple: 	http_get_simple.o
	$(CC) -o $@ $^ $(LIBS)

http_get_simple.o:	http_get_simple.c

http_get_options: 	http_get_options.o
	$(CC) -o $@ $^ $(LIBS)

http_get_options.o:	http_get_options.c

http_get: 	http_get.o
	$(CC) -o $@ $^ $(LIBS)

http_get.o:	http_get.c

json_pprint: 	json_pprint.o
	$(CC) -o $@ $^ $(LIBS)

json_pprint.o:	json_pprint.c

clean:
	rm http_get.o http_get http_get_options.o http_get_options http_get_simple.o http_get_simple
