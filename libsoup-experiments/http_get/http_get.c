# include <stdio.h>
# include <stdlib.h>
# include <libsoup/soup.h>

#define BUF_SIZE 65520

int main(int argc, char **argv)
{
  SoupSession *session;
  SoupRequestHTTP *request;
  GError *error;
  GInputStream *response;
  char buf[BUF_SIZE];
  gsize read_bytes;
  int i;

  session = soup_session_new_with_options(SOUP_SESSION_USER_AGENT, "libsoup", NULL);
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
  if (! g_input_stream_read_all (response,
				 &buf,
				 BUF_SIZE,
				 &read_bytes,
				 NULL,
				 &error)) {
    printf("Error reading the response\n");
    exit(1);
  }

  for(i=0; i<read_bytes; i++)
    printf("%c", buf[i]);
  printf("\n");

  return 0;
}
