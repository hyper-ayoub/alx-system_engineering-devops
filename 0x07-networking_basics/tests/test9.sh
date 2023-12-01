$tail -f txt1 &

$ jobs
[1]+ Running tail -f txt1.log  &      ### still running in background

$echo $!    ### get the process id 
5378

$ps -ef | grep 5378  #### confirm if this is the same process id
work 5378 4406 0 23:33 pts/0 00:00:00 tail -f txt1.log
