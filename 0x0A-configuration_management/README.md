#0x0A-configuration_management
![Kskg37qnPTwy2USC5b8721io](https://github.com/hyper-ayoub/alx-system_engineering-devops/assets/133155846/cbf4e921-1e53-401b-a6e2-83dd73845827)


#installation :

                 apt-get install -y ruby=1:2.7+1 --allow-downgrades
                 apt-get install -y ruby-augeas
                 apt-get install -y ruby-shadow
                 apt-get install -y puppet
                 
#Install puppet-lint 

                  gem install puppet-lint



#Overview of Popular Tools 

![Capture d’écran 2024-01-19 204803](https://github.com/hyper-ayoub/alx-system_engineering-devops/assets/133155846/081ad620-4c34-4d7a-833b-49b2e4f521b6)

#Puppet lint
     
Install It!
 
               package { 'puppet-lint':
                 ensure   => '1.1.0',
                 provider => 'gem',
                  }

                    
#Or: 

          gem install puppet-lint




#Run It!  


                  puppet-lint /etc/puppet/modules

                 
Fix Them!


                  puppet-lint --fix /etc/puppet/modules
#Resource Type file: 

Attributes

Providers

Provider Features

                     https://www.puppet.com/docs/puppet/5.5/types/file.html



