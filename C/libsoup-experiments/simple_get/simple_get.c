# include <stdio.h>
# include <libsoup/soup.h>

int main(int argc, char **argv)
{
  SoupSession *session = soup_session_new();
  SoupMessage *request;
  int status;

  /* Create a GET request*/
  request = soup_message_new ("GET", argv[1]);
  /* Send the GET request and wait for response */
  status = soup_session_send_message (session, request);
  if (status != 200) {
    printf("Error: Recieved %u from server\n", status);
  }
  else {
    fwrite (request->response_body->data,
	    request->response_body->length,
	    1, stdout);
  }
  return 0;
}
