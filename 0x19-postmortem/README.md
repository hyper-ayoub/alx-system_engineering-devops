
# 🕷️Postmortem
Project from holberton School





# 👁️ What is an Incident Postmortem?
A postmortem (or post-mortem) is a process intended to help you learn from past incidents. It typically involves an analysis or discussion soon after an event has taken place.

Postmortems typically involve blame-free analysis and discussion soon after an incident or event has taken place. An artifact is produced that includes a detailed description of exactly what went wrong in order to cause the incident, along with a list of steps to take in order to prevent a similar incident from occurring again in the future. An analysis of how your incident response process itself worked during the incident should also be included in the discussion. The value of postmortems comes from helping institutionalize a culture of continuous improvement. This way, teams are better prepared when another incident inevitably occurs with mission- or business-critical systems.

As your systems scale and become more complex, failure is inevitable, assessment and remediation is more involved and time-consuming, and it becomes increasingly painful to repeat recurring mistakes. Not having data when you need it is expensive.

Streamlining the postmortem process is key to helping your team get the most from their postmortem time investment: spending less time conducting the postmortem, while extracting more effective learnings, is a faster path to increased operational maturity. In fact, the true value of postmortems comes from helping institutionalize a positive culture around frequent and iterative improvement.



# 👁️Why Do Postmortems?
During incident response, the team is 100% focused on restoring service. They should not be wasting time and mental energy thinking about how to do something optimally or performing a deep dive on what caused the incident. Doing this could further delay remediation efforts and convolute the resolution process. That’s why postmortems are essential—they provide a peacetime opportunity to reflect once the issue is no longer impacting users. The postmortem process drives focus, instills a culture of learning, and identifies opportunities for improvement that otherwise would be lost.

Without a postmortem you fail to recognize what you’re doing right, where you could improve, and most importantly, how to avoid making the same mistakes in the future. Writing an effective postmortem allows you to learn quickly from your mistakes and improve your systems and processes. A well-designed, blameless postmortem allows teams to continuously learn, serving as a way to iteratively improve your infrastructure and incident response process. Be sure to write detailed and accurate postmortems in order to get the most benefit out of them.


# 👁️When Do You Do a Postmortem?

Teams should conduct a postmortem after every major incident (any incident that is a Sev-2 or Sev-1). This includes any time incident response is triggered–even if it is later discovered that severity was actually lower, it was a false alarm, or it quickly recovered without intervention. A postmortem should not be neglected in these cases because it is still an opportunity to review what did and did not work well in the incident response process. If the incident should not have triggered incident response, it is worthwhile understanding why it did so monitoring can be tuned to avoid unnecessarily triggering incident response in the future. Doing this analysis and follow-up action will help prevent alert fatigue going forward.


# 👁️Who Is Responsible for the Postmortem?
At the end of a major incident call, or very shortly after, the Incident Commander selects and directly notifies one responder to own the postmortem. Note that the postmortem owner is not solely responsible for completing the postmortem themselves. Writing a postmortem is a collaborative effort and should include everyone involved in the incident response. While engineering will lead the analysis, the postmortem process should involve management, customer support, and business communications teams. The postmortem owner coordinates with everyone who needs to be involved to ensure it is completed in a timely manner.





## 🕵️ FAQ

#### Steps to Write your  first postemortem  #####

## 📚Issue Summary

short summary (5 sentences)
list the duration along with start and end times (include timezone)
state the impact (most user requests resulted in 500 errors, at peak 100%)
close with root cause

## 📚Timeline

list the timezone
covers the outage duration
when outage began
when staff was notified
actions, events, …
when service was restored

## 📚Root Cause

give a detailed explanation of event
do not sugarcoat

## 📚Resolution and recovery

give detailed explanation of actions taken (includes times)

## 📚Corrective and Preventative Measures

itemized list of ways to prevent it from happening again
what can we do better next time?





# 🎩this is my first postemortem that i create 

### 🧶0x18. Webstack monitoring

 https://www.datadoghq.com/ 

  1: For this project we need to 
 Sign up for Datadog and install datadog-agent

 2: Monitor some metrics  (add monitors)

 3:
 Create a dashboard


### 🧤Issue Summary

From Mar 6, 2024 4:00 AM to Mar 7, 2024 4:00 AM

So when  I want to install datadog in web-1  (ubuntu) with the prv keys 
the installation is done but the datadog is not working 
thats mean we have Issue with server or the install keys is not working 
and if we will not running the datadog all complemeted  tasks is not working



### 🧤Timeline (all times Pacific Time)
📌4:00 PM: Start understanding the concept of datadog

📌4:26 PM: take all steps (or) commands line to start installing

📌5:00 PM: Configuration of my web-1 should be clean before start (nginx)

📌5:12 PM: Start install datadog (take the keys and put it to my own server) still wating

📌5:30 PM: Successful the installation completed now we need to test (sudo systemctl start datadog-agent)

📌5:31 PM: oh no is not working the status fails  (try to debugging)

📌5:40 PM: fixing the nginx Configuration and take another key (update the environement)

sudo vi /etc/nginx/
(check all files)

sudo apt-get update && sudo service nginx restart 


📌5:50 PM : Start to generate the key and put it to the server as a command line

📌6:10 PM : wating ....  (done)  

📌6:12 PM : Testing ✔ Finally we did it is running  (sudo systemctl start datadog-agent)
we can approved that -> we see a green title 

### 🧤Root Cause

Starting from 

5:00 PM we did not check the Configuration of nginx and start install
that menn the Configuration is not according to be a good environement to  install
datadog because the keys is requesting the server to run it as a command after creating an account to https://www.datadoghq.com/

### 🧤Resolution and recovery

Don't forget before any installation make sure to create a backup of your tasks
like config, keys, scripts ...
because the backup help you to return the old actions that you did and you forget to save it so when you have some Issue backup is your Heros

### 🧤Corrective and Preventative Measures

### 🧤Itemized list of ways to prevent it from happening again 
### what can we do better next time?

☛ Fixing all files (config, key...)

☛ backup

☛ don't start without background (concept)

☛ service should be running (example with datadog)

⚫ sudo systemctl start datadog-agent

☛ Check Status ✔ 







![Colorful Minimalist Linear Steps Circular Diagram](https://github.com/hyper-ayoub/alx-system_engineering-devops/assets/133155846/af977645-75c9-476e-8969-38a6bbe88c79)




 ![IMMKT-153-illustration-for-postmortem-page](https://github.com/hyper-ayoub/alx-system_engineering-devops/assets/133155846/bc1358a6-4e70-4c5f-963e-0e193076b104)





