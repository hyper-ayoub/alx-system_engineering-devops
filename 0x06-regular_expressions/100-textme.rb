#!/usr/bin/env ruby
#The sender phone number or name (including country code if present)
#The receiver phone number or name (including country code if present.
puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
