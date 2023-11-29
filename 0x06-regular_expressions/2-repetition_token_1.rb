#!/usr/bin/env ruby
#create a Ruby script that accepts one argument and pass it to a regular expression
puts ARGV[0].scan(/hb?tn/).join
