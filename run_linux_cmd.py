import subprocess #module to use linux commands
import logging #

logging.basicConfig(level=logging.INFO, format='| %(levelname)-15s | %(asctime)s | %(name)s | %(lineno)-4s ::  %(message)s')

logger = logging.getLogger("test") #get logger is also built in function

# Define the command you want to execute, passing the multiple cmds so using the list
command = [
       'grep -rl "org" *',
       'ls',
       'pwd'
       ]

# Run the command
#The stdout=subprocess.PIPE parameter captures the output of the command, which you can then access using result.stdout.
for cmd in command:
    result = subprocess.run(cmd, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #run is used to run the linux cmds
  # Print the output
    logger.info(result.stdout)
    print(result.stderr, end='')
