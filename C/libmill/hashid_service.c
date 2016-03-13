/* Coroutine based HTTP server implements hashid as service (http://hashids.org/c/) */

#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <libmill.h>
#include <string.h>

coroutine void serve(tcpsock as) {

    int64_t deadline = now() + 10000;
    char inbuf[256];
    char outbuf[256];

    char *response;
    int resp_nbytes;

    /* Recieve data until either the buffer is full or \r is encountered */
    size_t sz = tcprecvuntil(as, inbuf, sizeof(inbuf), "\r", 1, deadline);
    if(errno != 0)
        goto cleanup;
    inbuf[sz - 1] = 0;

    /* Parse the incoming request  (Example: GET /index.html HTTP/1.1)*/

    // First find if we support the HTTP method requested
    char http_method[5];
    int pos;
    for(pos=0; pos < sz; pos++) {
      if (inbuf[pos] == ' ') {
        break;
      } else {
        // We can do better
        http_method[pos] = inbuf[pos];
      }
    }
    http_method[pos] = 0;

    if (strcmp(http_method, "GET") != 0) {
      response = "Method not supported\r\n";
      resp_nbytes = snprintf(outbuf, sizeof(outbuf), "%s", response);
    } else {
      response = "Hello, there\r\n";
      resp_nbytes = snprintf(outbuf, sizeof(outbuf), "%s", response);
    }

    sz = tcpsend(as, outbuf, resp_nbytes, deadline);
    if(errno != 0)
        goto cleanup;
    tcpflush(as, deadline);

    if(errno != 0)
        goto cleanup;

    cleanup:
    strerror(errno);

    tcpclose(as);
}

int main(int argc, char *argv[]) {

    int port = 5555;
    ipaddr addr = iplocal(NULL, port, 0);
    tcpsock ls = tcplisten(addr, 10);
    if(!ls) {
        perror("Can't open listening socket");
        return 1;
    }

    printf("Listening for HTTP connections on port %d\n", port);

    while(1) {
        tcpsock as = tcpaccept(ls, -1);
        if(!as)
            continue;
        go(serve(as));
    }
}

