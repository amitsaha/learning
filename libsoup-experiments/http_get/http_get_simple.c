# include <stdio.h>
# include <stdlib.h>
# include <libsoup/soup.h>

#define BUF_SIZE 65000

int main(int argc, char **argv)
{
  SoupSession *session;
  SoupRequestHTTP *request;
  GError *error;
  GInputStream *response;
  char buf[BUF_SIZE];
  int read_bytes, i;

  session = soup_session_new();
  /* Create a HTTP request */
  request = soup_session_request_http (session,
				       "GET",
				       argv[1],
				       &error);
  if (request == NULL) {
    printf("Couldn't create request\n");
    exit(1);
  }
  /* Send the request synchronously */
  response = soup_request_send((SoupRequest *) request, NULL, &error);
  read_bytes = g_input_stream_read (response,
				    &buf,
				    BUF_SIZE,
				    NULL,
				    &error);
  if (read_bytes == -1) {
    perror("Error reading response");
    exit(1);
  }
  for(i=0; i<read_bytes; i++)
    printf("%c", buf[i]);
  printf("\n");
  
  return 0;
}
