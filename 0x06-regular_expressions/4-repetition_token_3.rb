#!/usr/bin/env ruby
#Ruby script that accepts one argument and pass it to a regular expression && Your regex should not contain square brackets.
puts ARGV[0].scan(/hbt*n/).join
