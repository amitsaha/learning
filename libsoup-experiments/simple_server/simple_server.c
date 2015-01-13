# include <stdio.h>
# include <stdlib.h>
# include <libsoup/soup.h>

int main(int argc, char **argv)
{
  SoupServer *server;
  GError *error;

  server = soup_server_new(SOUP_SERVER_SERVER_HEADER, "simple-server",
			   NULL);
  if (!soup_server_listen_local(server,
				8080,
				SOUP_SERVER_LISTEN_IPV4_ONLY,
				&error)) {
    printf("Could not start server for listening\n");
    exit(1);
  }

  printf("Server listening on 127.0.0.1:8080\n");

  /* Setup the GMainLoop*/
  GMainLoop* main_loop = NULL;
  main_loop = g_main_loop_new (NULL, FALSE);
  g_main_loop_run(main_loop);
  return 0;
}
  
