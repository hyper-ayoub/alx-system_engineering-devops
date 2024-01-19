#!/usr/bin/pup
# install a package Flask (2.0.1)
package { 'flask':
  ensure => '2.1.0',
  provider => 'pip3',
}
