#install a package Flask

package { 'flask':
  ensure => '2.1.0',
  provider => 'flask',
}
