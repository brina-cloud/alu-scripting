#!/usr/bin/env ruby
log_line = ARGV[0]
sender = log_line.match(/\[from:([^\]]+)\]/)&.captures&.first
receiver = log_line.match(/\[to:([^\]]+)\]/)&.captures&.first
flags = log_line.match(/\[flags:([^\]]+)\]/)&.captures&.first
puts "#{sender},#{receiver},#{flags}"

