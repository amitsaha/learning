# List the files and directories in the current directory

d = Dir.new(".")
d.each { |x| puts "Got #{x}" }

# Or get as an array
entries = Dir.entries(".")
entries.each { |file| puts "Got #{file}"}
