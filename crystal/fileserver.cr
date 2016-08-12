require "http/server"

server = HTTP::Server.new("0.0.0.0", 8080) do |context|
  context.response.content_type = "text/plain"
  http_method = context.request.method
  if http_method != "GET"
      # Bad request
      context.response.status_code = 400
      context.response.print "Only GET supported"
  end

  request_path = context.request.path
  if request_path == "/"
      entries = Dir.entries(".")
      context.response.status_code = 200
      entries.each {|file| context.response.print file}
  else
      # Check if the requested path exists relative to the current directory
      path = File.join(".", request_path)
      if File.exists?(path)
          # If it's a file, return the file contens with the right
          # mimetype
          if File.file?(path)
              context.response.print "File contents"
          end

          if File.directory?(path)
              entries = Dir.entries(".")

              context.response.status_code = 200
              entries.each {|file| context.response.print file}
          end
      else
          context.response.status_code = 404
      end
  end 

end

puts "Listening on http://0.0.0.0:8080"
server.listen
