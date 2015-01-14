# include <stdio.h>
# include <stdlib.h>
# include <json-glib/json-glib.h>

void pprint(char *buf)
{
  JsonParser *parser = json_parser_new ();
  JsonGenerator *generator = json_generator_new ();
  JsonNode *root;
  gsize len;
  char *data;
  json_generator_set_pretty (generator, TRUE);
  json_generator_set_indent (generator, 1);
  json_generator_set_indent_char (generator, '\t');

  if (!json_parser_load_from_data (parser, buf, -1, NULL)) {
    printf("Could not parse JSON data\n");
    exit(1);
  }

  root = json_parser_get_root(parser);
  json_generator_set_root(generator, root);
  data = json_generator_to_data (generator,  &len);
  g_print(data);

}

int main(int argc, char **argv)
{
  char *buf = "{\n"
    "\t\"foo\" : 42,\n"
    "\t\"bar\" : true,\n"
    "\t\"baz\" : null\n"
    "}";
  
  pprint(buf);
  return 0; 
}

